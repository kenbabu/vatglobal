import csv
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
import django_filters.rest_framework
import  django_filters
from rest_framework import status
from .serializers import (
    FileSerializer,
    TransactionSerializer,
)
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import datetime
from datetime import datetime
from dateutil import  parser
from .models import (
    CSVFile,
    Transaction,
    Currency,
) 
from .forms import  CSVModelForm
from django.http import  HttpResponse
import  csv

# Helper functions for validations
from .utilities import helperfunctions as hf


class HomeView(TemplateView):
    template_name = "vat_app/home.html"

def uploadFileView(request):
    # ('vat_app/upload.html')
    form = CSVModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CSVModelForm()
        
        obj = CSVFile.objects.get(activated=False )

        transactions=[]
        with open(obj.file_name.path, 'r') as f:
            reader = csv.DictReader(f)
            next(reader)
            count = 0
            
            for row in reader:
                # print(row['Date'], type(row['Date']))
                date = row['Date']
                description = row['Purchase/Sale']
                country = row['Country']
                currency = row['Currency']
                net = float(row['Net'])
                vat = float(row['VAT'])
                # Ignore erroneous rows - could be saved to a log file for error checking
                if not hf.valid_date(date) or not hf.get_description(description):
                    continue
                parsed_date = parser.parse(date).date()
                record = Transaction(trans_date=parsed_date, description=hf.get_description(description), country=country,
                                         currency=currency, net=net,vat=vat)

                transactions.append(record)
                # Bulk create to avoid hitting the database numerous times
        Transaction.objects.bulk_create(transactions)
        # Transaction.objects.bulk_create(topten) 
        obj.activated = True
        obj.save()
    return render(request,'vat_app/upload.html', {'form':form})



class TransactionFilter(django_filters.FilterSet):
    vat = django_filters.NumberFilter()
    net = django_filters.NumberFilter()

    min_vat = django_filters.NumberFilter(field_name="vat", lookup_expr='gte')
    max_vat = django_filters.NumberFilter(field_name="vat", lookup_expr='lte')
    min_net = django_filters.NumberFilter(field_name="net", lookup_expr='gte')
    max_net = django_filters.NumberFilter(field_name="net", lookup_expr='lte')
    trans_year = django_filters.NumberFilter(field_name="trans_date", lookup_expr='year')
    # date = django_filters.NumberFilter(field_name="trans_date", lookup_expr='iexact')
    class Meta:
        model = Transaction
        fields = ['country','description','currency', 'vat', 'net', 'trans_date']


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['country','description','currency', 'vat', 'net','date']
    filter_class = TransactionFilter
    


    
