# -*- coding: utf-8 -*-
"""Client-side wrapper lib around GeoIP.

By using this we make the geoip module optional. ie. don't fail if the user opts out of using
GEOIP.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from django.contrib.gis.geoip2 import GeoIP2
    from geoip2.errors import AddressNotFoundError

    geoip_available = True
except ImportError:
    geoip_available = False

try:
    from pycountry import countries
except ImportError:
    if getattr(settings, "IPRESTRICT_GEOIP_ENABLED", True):
        raise ImproperlyConfigured(
            "You are using location based IP Groups, but the python package "
            "pycountry isn't installed. Please install pycountry or set 'IPRESTRICT_GEOIP_ENABLED' "
            "to False in settings.py"
        )


# Special value for IP addresses that have no country like localhost.
# Using the 'XX' special value allows for rules being set up on the 'XX' country code
# and giving more control to end-users on what to do for special cases like this
NO_COUNTRY = "XX"


class AdaptedGeoIP2(object):
    """Makes GeoIP2 behave like GeoIP"""

    def __init__(self, *args, **kwargs):
        self._geoip = GeoIP2()

    def country_code(self, ip):
        # if the IP isn't in the DB return None instead of throwing an Exception as GeoIP does
        try:
            return self._geoip.country_code(ip)
        except AddressNotFoundError:
            return None


class OurGeoIP(object):
    def country_code(self, ip):
        raise ImproperlyConfigured(
            "You are using location based IP Groups, "
            "but 'IPRESTRICT_GEOIP_ENABLED' isn't set to True in settings.py"
        )


_geoip = OurGeoIP()
if getattr(settings, "IPRESTRICT_GEOIP_ENABLED", True):
    if not geoip_available:
        raise ImproperlyConfigured(
            "'IPRESTRICT_GEOIP_ENABLED' is set to True, but geoip2 is NOT available "
            " to import. Make sure the geoip libraries are installed as described in the Django "
            "documentation"
        )
    _geoip = AdaptedGeoIP2()


def get_geoip():
    return _geoip


def is_valid_country_code(code):
    if code == NO_COUNTRY:
        return True
    country = countries.get(alpha_2=code)
    return country is not None
