from django.urls import URLPattern, path 
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home')
]