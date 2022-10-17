from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from ... import models


class Command(BaseCommand):
    help = "Replaces the current rules in the DB with the rules in the given fixture file(s)."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "args", metavar="fixture", nargs="+", help="Fixture labels."
        )

    def handle(self, *args, **options):
        with transaction.atomic():
            self.delete_existing_rules()
            call_command("loaddata", *args, **options)

    def delete_existing_rules(self):
        models.Rule.objects.all().delete()
        models.IPRange.objects.all().delete()
        models.IPGroup.objects.all().delete()
