from django import  forms
from .models import CSVFile 
from django.utils.translation import gettext_lazy as _

class CSVModelForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ('file_name',)
        # labels = {
        #     'file_name': _('Data File')
        # }