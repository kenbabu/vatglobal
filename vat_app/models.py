from django.db import models
from django.core.exceptions import ValidationError
from dateutil import parser
from datetime import  datetime
# Create your models here.
class CSVFile(models.Model):
    file_name = models.FileField(blank=False, null=False,upload_to='csvs' )
    timestamp = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

def validate_currency(value):
    pass
def is_valid_date(value, fuzzy=False):
    try:
        parser.parse(value, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def validate_2020_records(value):
    date_str = parser.parse(value,'%Y/%m/%d')
    year = datetime.strftime(date_str, '%Y')
    if year != '2020':
        raise ValidationError(_('Only 2020 records'),
        params={'value': value},
        )
        # good date

class Currency(models.Model):
   code = models.CharField(blank=True, max_length=10)
   description = models.CharField(blank=True, max_length=100)

   def __str__(self):
       return self.code
   
        
class Transaction(models.Model):
    trans_date = models.DateTimeField()
    # trans_date = models.DateTimeField()
    description = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    currency = models.CharField(max_length=3, blank=True)
    net = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    trans_year = models.CharField(blank=True, max_length=20)


    def __str__(self):
        return f"{self.id}"
    def get_trans_year(self):
        return self.trans_date.strftime('%Y')
    def formatted_date(self):
        return self.trans_date.strftime('%Y/%m/%d')
    
    def save(self, *args, **kwargs):
        self.trans_year = self.get_trans_year()
        self.trans_date = self.formatted_date()
        super(Transaction, self).save(*args, **kwargs)

    