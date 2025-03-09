
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
 path('home/', views.index, name='home'),
 path('resume/', views.resume, name='resume'),
]