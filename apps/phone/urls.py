from django.urls import path
from . import views

urlpatterns = [
    path("", views.p_list, name="p_list"),
    path("add/", views.Get_phone, name="Get_phone"),
    path("<slug:slug>/", views.details, name="details"),
    path("<slug:slug>/edit/", views.edit_phone, name="edit_phone"),
    path("<slug:slug>/delete/", views.delete_phone, name="delete_phone"),
]