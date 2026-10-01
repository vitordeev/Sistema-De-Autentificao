# 🔐 Projeto de Autenticação com Django

Sistema de autenticação desenvolvido com **Python** e **Django**, criado com o objetivo de praticar conceitos fundamentais de desenvolvimento Full Stack.

O projeto implementa um fluxo completo de autenticação de usuários, incluindo cadastro, login, logout e recuperação de senha.

---

## 🚀 Funcionalidades

- Cadastro de usuários
- Validação de e-mail já cadastrado
- Validação de confirmação de senha
- Login com e-mail e senha
- Logout
- Proteção de páginas com autenticação
- Sistema de mensagens de sucesso e erro
- Recuperação de senha
  - Geração de código de verificação
  - Validação do código de recuperação
  - Redefinição de senha
- Armazenamento de informações adicionais do usuário

---

## 🛠️ Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- SQLite
- Django ORM
- Git e GitHub

---

## 📂 Estrutura do projeto

```text
projeto-autenticacao/
│
├── accounts/
│   ├── migrations/
│   ├── static/
│   │   └── accounts/
│   │       └── css/
│   ├── templates/
│   │   └── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd projeto-autenticacao
```

### 3. Crie o ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Depois, acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Fluxo de autenticação

### Cadastro e login

```text
Cadastro
   ↓
Login
   ↓
Home protegida
   ↓
Logout
```

### Recuperação de senha

```text
Recuperar senha
      ↓
Informar e-mail
      ↓
Gerar código
      ↓
Validar código
      ↓
Definir nova senha
      ↓
Login
```

---

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos em Django e desenvolvimento Full Stack.

O principal objetivo foi colocar em prática conceitos como:

- Views
- Templates
- URLs
- Formulários
- Requisições GET e POST
- Sessões
- Django ORM
- Models
- Autenticação
- Sistema de mensagens
- Proteção de rotas
- Manipulação de senhas
- Recuperação de senha

---

## 👨‍💻 Autor

**Victor Gabriel**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento Full Stack.

---

## 📌 Status

✅ **Concluído** — Projeto de estudo

Novas funcionalidades podem ser adicionadas futuramente conforme o avanço dos estudos em Django.
