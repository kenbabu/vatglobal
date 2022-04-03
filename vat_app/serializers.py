from rest_framework import serializers
from .models import (
    CSVFile,
    Currency,
    Transaction,
)

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = CSVFile 
        fields = ('file_name', )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'