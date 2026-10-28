# 🔐 Projeto de Autenticação com Django

Sistema de autenticação desenvolvido com **Python** e **Django**, criado com o objetivo de praticar conceitos fundamentais de desenvolvimento Full Stack.

O projeto implementa um fluxo completo de autenticação de usuários, incluindo cadastro, login, logout e recuperação de senha.

<<<<<<< HEAD
=======
---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
## 🚀 Funcionalidades

- Cadastro de usuários
- Validação de e-mail já cadastrado
- Validação de confirmação de senha
- Login com e-mail e senha
- Logout
- Proteção de páginas com autenticação
- Sistema de mensagens de sucesso e erro
- Recuperação de senha
<<<<<<< HEAD
- Geração de código de verificação
- Validação do código de recuperação
- Redefinição de senha
- Armazenamento de informações adicionais do usuário

=======
  - Geração de código de verificação
  - Validação do código de recuperação
  - Redefinição de senha
- Armazenamento de informações adicionais do usuário

---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
## 🛠️ Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- SQLite
- Django ORM
- Git e GitHub

<<<<<<< HEAD
=======
---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
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

<<<<<<< HEAD
=======
---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
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

<<<<<<< HEAD
Depois, acesse:

<http://127.0.0.1:8000/>
=======
Depois, acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---
>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b

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

<<<<<<< HEAD
=======
---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
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

<<<<<<< HEAD
=======
---

>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b
## 👨‍💻 Autor

**Victor Gabriel**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento Full Stack.

<<<<<<< HEAD
## 📌 Status

**Concluído — Projeto de estudo**
=======
---

## 📌 Status

✅ **Concluído** — Projeto de estudo
>>>>>>> f258f8c693e2d7f7164f7bcbf1af92b5b514032b

Novas funcionalidades podem ser adicionadas futuramente conforme o avanço dos estudos em Django.
