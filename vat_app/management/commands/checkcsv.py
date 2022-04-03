from django.core.management.base import BaseCommand, CommandError
from dateutil import  parser
# vat_app.models import Transaction
import csv

def valid_date(str_date):
    res = True
    try:
        res = bool(parser.parse(str_date))
    except ValueError:
        res = False
    return res



class Command(BaseCommand):
    help = 'Check a csv for errors.'

    def add_arguments(self, parser, *args):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **options):
        try:
            with open(options['filepath']) as csvfile:
               data = csv.reader(csvfile) 
               next(data)
               list_of_rows = list(data)
               for line in list_of_rows:
                #    print(valid_date(line[0]))
                    if  not valid_date(line[0]):
                        print(line)
            # return list_of_rows
        except FileNotFoundError:
            print(f"File {options['filepath']} not found")
