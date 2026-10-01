
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Perfil
import random 
from django.core.mail import send_mail
from django.contrib import messages

#funcoes do login da aplicação
def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if not email or not senha:
            messages.error(request, "Preencha email e senha.")
            return render(request, "accounts/index.html")

        usuario = User.objects.filter(email=email).first()

        if usuario:
            print(f"Usuario encontrado: {usuario.username}")
            print(f"Email encontrado: {usuario.email}")

            usuario_autenticado = authenticate(
                request,
                username=usuario.username,
                password=senha
            )

            if usuario_autenticado:
                auth_login(request, usuario_autenticado)
                print("Login realizado")
                return redirect("home")

            else:
                messages.error(request, "Email ou senha incorretos.")
                return render(request, "accounts/index.html")

        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, "accounts/index.html")

    return render(request, "accounts/index.html")


#funcao do propio django para entrar na home tem que estar logado
@login_required
def home(request):
    return render(request, 'accounts/home.html' )


#Funcao para dar logout usando os imports do propio django
def sair(request):
    logout(request)
    return redirect("login")

#Funcoes do Cadastro:
def cadastro(request):

    if request.method == "POST":

        email = request.POST.get("Cadastro-Email")
        senha = request.POST.get("CadastroSenha")
        confirmarsenha = request.POST.get("Repetir-Senha")
        telefone = request.POST.get("Cadastro-Telefone")
        cep = request.POST.get("cep")
        rua = request.POST.get("rua")
        numero = request.POST.get("casa")

        usuario = User.objects.filter(email=email).first()

        if usuario:
            messages.error(request, "Usuario já esta cadastrado.")
            return render(request, "accounts/cadastro.html")

        if senha != confirmarsenha:
            messages.error(request, "As senhas informadas não são iguais.")
            return render(request, "accounts/cadastro.html")

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=senha
        )

        Perfil.objects.create(
            usuario=usuario,
            cep=cep,
            rua=rua,
            numero=numero,
            telefone=telefone
        )

        return  redirect("/login")
    return render(request, "accounts/cadastro.html")

#Funcao de nova senha 
def novaSenha(resquest):
    return render(resquest , "accounts/novaSenha.html")

#Funcao do codigo de verificação e da de verificar o email 
def recuperarSenha(resquest):
    if resquest.method == "POST":

        if resquest.GET.get("novo") == "1":
            resquest.session.pop("email-recuperacao", None)

        email = resquest.POST.get("rpemail")
        acao = resquest.POST.get("acao")
        usuario = User.objects.filter(email=email).first()

        if acao == "enviar":
            if not usuario:
                messages.error(resquest, "E-mail não encontrado.")
                return render(resquest,"accounts/recuperarSenha.html",{"email": email})
            
            codigo = random.randint(100000, 999999)
            resquest.session["email-recuperacao"] = email
            resquest.session["codigo-recuperacao"] = str(codigo)
            messages.success(resquest, "Codigo enviado com sucesso")
            send_mail(
                "Código de recuperação de senha",
                f"Seu código de recuperação é: {codigo}",
                "noreply@meusite.com",
                [email],)

        elif acao == "verificar":
            codigo_digitado = resquest.POST.get("rpsenha")
            codigo_salvo = resquest.session.get("codigo-recuperacao")

            print(codigo_digitado)
            print(codigo_salvo)

            if codigo_salvo == codigo_digitado:
                messages.success(resquest, "Os codigo informado esta correto")
                return redirect("novasenha")

            else:
                messages.error(resquest, "Os codigo informado esta errado")
    email = resquest.session.get("email-recuperacao", "")
    return render(
        resquest,
        "accounts/recuperarSenha.html",
        {"email": ''}
    )

def novasenha(request):

    if request.method == "POST":
        

        email = request.session.get("email-recuperacao")

        senha = request.POST.get("novasenha")
        senha_confirmada = request.POST.get("Cnovasenha")

        usuario = User.objects.get(email=email)

        if senha == senha_confirmada:

            usuario.set_password(senha_confirmada)
            usuario.save()

            return redirect("login")
        
        else:
            messages.error(request, "As senhas não são iguais!")

    return render(request, "accounts/novaSenha.html")
   
# Create your views here.
