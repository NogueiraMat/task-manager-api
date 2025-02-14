# Task Manager API  

Task Manager API é uma API desenvolvida com **FastAPI** para gerenciamento de tarefas. Utiliza **PostgreSQL** como banco de dados, **SQLAlchemy** para ORM e **Alembic** para controle de migrações. A API permite criar, listar, atualizar e excluir tarefas, além de autenticação de usuários via **JWT**.  

O projeto é **containerizado com Docker** e orquestrado com **Docker Compose**, facilitando a configuração e execução dos serviços.  

## 📌 Tecnologias utilizadas  

- **[FastAPI](https://fastapi.tiangolo.com/)** – Framework web moderno e de alta performance para Python.  
- **[PostgreSQL](https://www.postgresql.org/)** – Banco de dados relacional utilizado para armazenar as informações.  
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – ORM para manipulação do banco de dados de forma programática.  
- **[Alembic](https://alembic.sqlalchemy.org/)** – Ferramenta para gerenciamento de migrações do banco de dados.  
- **[Docker](https://www.docker.com/)** – Plataforma para criação e gerenciamento de contêineres.  
- **[Docker Compose](https://docs.docker.com/compose/)** – Ferramenta para definir e rodar aplicações multi-contêiner.  

## 🚀 Como executar o projeto  

### 🛠️ Pré-requisitos  
Antes de iniciar, certifique-se de ter instalado:  

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

### 📂 Configuração e execução  

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/task-manager-api.git
   cd task-manager-api
   ```

2. Suba os contêineres com o Docker Compose:  
   ```bash
   docker-compose up --build
   ```

3. Acesse a documentação interativa do FastAPI no navegador:  
   ```
   http://localhost:8000/docs
   ```

### 🔄 Rodando migrações do banco de dados  

Se precisar rodar as migrações manualmente, utilize o seguinte comando dentro do contêiner da API:  

```bash
docker exec -it task-manager-api alembic upgrade head
```

### 📌 Observações  

- O arquivo **`docker-compose.yml`** já define os serviços necessários para rodar a API, incluindo o banco de dados PostgreSQL.  
- O serviço da API está configurado para rodar na porta `8000`.  

## 📜 Licença  

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
