import logging
import warnings

from django.conf import settings
from django.core import exceptions

from .ip_utils import is_valid_ip_address
from .models import ReloadRulesRequest
from .restrictor import IPRestrictor

logger = logging.getLogger(__name__)


UNKNOWN = "unknown"


class IPRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.restrictor = IPRestrictor()
        self.trusted_proxies = tuple(
            get_setting("IPRESTRICT_TRUSTED_PROXIES", "TRUSTED_PROXIES", [])
        )
        self.reload_rules = get_reload_rules_setting()
        self.ignore_proxy_header = bool(
            get_setting("IPRESTRICT_IGNORE_PROXY_HEADER", "IGNORE_PROXY_HEADER", False)
        )
        self.trust_all_proxies = bool(
            get_setting("IPRESTRICT_TRUST_ALL_PROXIES", "TRUST_ALL_PROXIES", False)
        )
        self.use_proxy_if_unknown = bool(
            getattr(settings, "IPRESTRICT_USE_PROXY_IF_UNKNOWN", False)
        )

    def __call__(self, request):
        if self.reload_rules:
            self.reload_rules_if_needed()

        url = request.path_info
        client_ip = self.extract_client_ip(request)
        if not is_valid_ip_address(client_ip):
            logger.warning(f"Denying access of {url} to INVALID IP")
            raise exceptions.PermissionDenied

        if self.restrictor.is_restricted(url, client_ip):
            logger.warning(f"Denying access of {url} to {client_ip}")
            raise exceptions.PermissionDenied

        response = self.get_response(request)
        return response

    def extract_client_ip(self, request):
        client_ip = request.META["REMOTE_ADDR"]
        if self.ignore_proxy_header:
            return client_ip

        forwarded_for = self.get_forwarded_for(request)
        if forwarded_for:
            client_ip = self.extract_client_ip_proxied_request(client_ip, forwarded_for)

        return client_ip

    def extract_client_ip_proxied_request(self, client_ip, forwarded_for):
        closest_proxy = client_ip
        client_ip = forwarded_for.pop(0)

        if client_ip == UNKNOWN:
            if self.use_proxy_if_unknown:
                client_ip = closest_proxy
            else:
                raise exceptions.PermissionDenied

        if self.trust_all_proxies:
            return client_ip

        proxies = [closest_proxy] + forwarded_for
        for proxy in proxies:
            if proxy not in self.trusted_proxies:
                logger.warning(
                    f"Client IP {client_ip} forwarded by untrusted proxy {proxy}"
                )
                raise exceptions.PermissionDenied

        return client_ip

    def get_forwarded_for(self, request):
        hdr = request.META.get("HTTP_X_FORWARDED_FOR")
        if hdr is None:
            return []
        return [ip.strip() for ip in hdr.split(",")]

    def reload_rules_if_needed(self):
        last_reload_request = ReloadRulesRequest.last_request()
        if last_reload_request is not None:
            if self.restrictor.last_reload < last_reload_request:
                self.restrictor.reload_rules()


def get_setting(new_name, old_name, default=None):
    setting_name = new_name
    if hasattr(settings, old_name):
        setting_name = old_name
        warn_about_changed_setting(old_name, new_name)
    return getattr(settings, setting_name, default)


def get_reload_rules_setting():
    if hasattr(settings, "DONT_RELOAD_RULES"):
        warn_about_changed_setting("DONT_RELOAD_RULES", "IPRESTRICT_RELOAD_RULES")
        return not bool(getattr(settings, "DONT_RELOAD_RULES"))
    return bool(getattr(settings, "IPRESTRICT_RELOAD_RULES", True))


def warn_about_changed_setting(old_name, new_name):
    # DeprecationWarnings are ignored by default, so lets make sure that
    # the warnings are shown by using the default UserWarning instead
    warnings.warn(
        "The setting name '%s' has been deprecated and it will be removed in a future version. "
        "Please use '%s' instead." % (old_name, new_name)
    )
