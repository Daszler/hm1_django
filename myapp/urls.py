from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='index'),
    path('about_me/', views.about_me, name='about'),
]