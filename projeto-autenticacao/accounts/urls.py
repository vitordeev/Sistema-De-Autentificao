
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    path('novaSenha/', views.novaSenha),
    path('recuperar-Senha/' , views.recuperarSenha)
]
