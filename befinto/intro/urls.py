from django.urls import path
from .views import *

urlpatterns = [
    path('',base, name='base'),
    path('index/',index,name='index'),
    path('add_book/', add_book, name='add_book'),

]