from django.urls import URLPattern, path 
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('valida_cadastro/', views.validar_cadastro, name="validar_cadastro"),
    path('valida_login/', views.validar_login, name="validar_login"),
    path('sair/', views.sair, name="sair")
    
]

