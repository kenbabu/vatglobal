from django.core.management.base import BaseCommand, CommandError
from vat_app.models import Transaction


class Command(BaseCommand):
    help = 'Check a csv for errors.'

    # def add_arguments(self, parser, *args):
    #     parser.add_argument('tbl_transaction', type=str)

    def handle(self, *args, **options):
        Transaction.objects.all().delete()
           