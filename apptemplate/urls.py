
from django.urls import path
from .views import *

urlpatterns = [
    path('temp1/', view_temp1, name='view_temp1'),
    path('temp2/', view_temp2, name='view_temp2'),
]