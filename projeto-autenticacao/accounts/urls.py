
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login , name = "login"),
    path('cadastro/', views.cadastro , name = "cadastro"),
    path('novaSenha/', views.novasenha, name = "novasenha"),
    path('recuperar_senha/' , views.recuperarSenha, name = "rpsenha"),
    path('home/', views.home, name='home' ),
    path("sair/", views.sair, name="sair"),
]
