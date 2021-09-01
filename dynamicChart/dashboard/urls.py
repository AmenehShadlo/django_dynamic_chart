from django.urls import path
from dashboard import views

urlpatterns = [
    path('index', views.indexView),
]