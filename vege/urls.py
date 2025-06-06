from django.contrib import admin
from django.urls import path
from vege import views

urlpatterns = [
    path('',views.receipes,name="receipes"),
    path('read_items',views.read_items,name="read_items"),
    path('delete-receipe/<int:id>/',views.delete_items,name="delete-receipe"),
    path('update-receipe/<int:id>/',views.update_receipe,name="update_receipe"),
]