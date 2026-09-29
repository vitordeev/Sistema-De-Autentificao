
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        print(email)
        print(senha)

        usuario = User.objects.filter(email=email).first()

        if usuario:
            print(f"Usuario encontrad0{usuario.username}")
            print(f'Email encontrado {usuario.email}')
                            
            usuario_autenticado = authenticate(
                request,
                username=usuario.username,
                password=senha
             
            )


            if usuario_autenticado:
                auth_login(request,usuario_autenticado)
                print("Login realizado")
            else:
                print("Login Invalido")
        else:
            print("Usuario nao encontrado")

    return render(request, "accounts/index.html")

def cadastro(resquest):
    if resquest.method == "POST":
        cadastroEmail = resquest.POST.get("Cadastro-Email")
        print(cadastroEmail)



    return render(resquest, "accounts/cadastro.html")

def novaSenha(resquest):
    return render(resquest , "accounts/novaSenha.html")

def recuperarSenha(resquest):
    return render(resquest, "accounts/recuperarSenha.html")


# Create your views here.
