from django.urls import path, include
from .views import (
     # FileView,
     uploadFileView,
     TransactionView,
     HomeView
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('retrieveRows', TransactionView, basename='Transaction')

app_name = 'vat_app'

urlpatterns = [
     # path('upload/', FileView.as_view(), name='file-upload'),
     path('processFile', uploadFileView, name='upload-csv'),
     # access url domain/transactions
     path('', HomeView.as_view(), name='home'), 
     path('api/', include(router.urls))
     
]
