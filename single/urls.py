from django.urls import path
from . import views

app_name = "single"

urlpatterns = [
    path("single/", views.single, name='single')
]