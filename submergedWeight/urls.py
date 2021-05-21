from django.urls import path
from .views import *

app_name = 'submergedWeight'

urlpatterns = [
    path('', layout, name='layout'),
]
