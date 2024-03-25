
from django.urls import path
from apps.kany.views import index

urlpatterns = [
    path('', index, name ='index_url')
]

