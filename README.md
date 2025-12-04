# Desafio Técnico - Estágio Python/Django 2026.1

Sistema de gerenciamento de alunos, cursos e matrículas. 

Desenvolvido por `@allysonliveira`

## 🚀 Tecnologias Utilizadas

* **Python 3.11** + **Django 5**
* **Django Rest Framework (DRF)** para API
* **PostgreSQL** (Banco de Dados)
* **Docker** & **Docker Compose**
* **HTML/CSS** (Django Templates)

## 📋 Pré-requisitos

* Docker e Docker Compose instalados.

## 🛠️ Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd desafio-dev-python

2. **Suba os containers (Aplicação + Banco de Dados): Este comando irá construir a imagem, aplicar as migrações e iniciar o servidor.**

   ```bash
   docker-compose up --build
    ```
    
    Aguarde até aparecer a mensagem de log indicando que o servidor iniciou em 0.0.0.0:8000.


3. **Crie um Superusuário (Para acessar o Admin): Em um novo terminal, execute:**

    ```bash
    docker-compose run --rm web python manage.py createsuperuser
    ```
    Siga as instruções para definir usuário e senha.

## 🔗 Acessando a Aplicação


### 🖥️ Frontend (e Relatórios HTML)

* **Frontend (Home):** [http://localhost:8000/](http://localhost:8000/)
* **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **Dashboard Geral:** [http://localhost:8000/api/dashboard/](http://localhost:8000/api/dashboard/)
* **Histórico de Alunos:** [http://localhost:8000/api/historico/](http://localhost:8000/api/historico/)


### 🔌 API Endpoints (DRF)
* **Raiz da API:** [http://localhost:8000/api/](http://localhost:8000/api/)
* **Alunos:** `/api/alunos/`
* **Cursos:** `/api/cursos/`
* **Matrículas:** `/api/matriculas/`
* **Relatório SQL Puro:** [http://localhost:8000/api/relatorio-cursos/](http://localhost:8000/api/relatorio-cursos/)

## 📂 Estrutura do Projeto

* `dev/`: Código fonte completo (Django + Templates).
* `meu_database.sql`: Dump da estrutura das tabelas (SQL).
* `docker-compose.yml`: Orquestração dos containers.

## ✅ Funcionalidades Extras Implementadas
* Consulta otimizada com **Raw SQL** (JOIN/GROUP BY) para relatório financeiro.
* Frontend integrado com navegação entre Dashboard e Admin.
* Estrutura de pastas semântica (`dev`).