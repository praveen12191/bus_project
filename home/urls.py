from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('get_location',views.get_loc,name="get_location"),
    path('not_exit',views.not_exit)
]
