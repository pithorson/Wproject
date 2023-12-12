
from django.contrib import admin
from django.urls import path
urlpatterns = [ 
    path('',views.home,name="Home"),
    path('delete/<CName>',views.delete_city,name="DCity")
]