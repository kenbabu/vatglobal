from django.contrib import admin
# from .models import File
from .models import CSVFile, Transaction,Currency

admin.site.register(CSVFile)
admin.site.register(Transaction)
admin.site.register(Currency)



