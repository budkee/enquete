# Roteiro para Projeto Django com Clean Architecture

## 1. Contexto da Aplicação

Esta aplicação tem como principal objetivo permitir que usuários cadastrados criem e gerenciem suas enquetes por categorias. Cada enquete terá perguntas com múltiplas opções de resposta, e os usuários poderão visualizar e votar nas enquetes disponíveis. A aplicação será uma API RESTful monolítica construída com Django, Docker e Once UI.

## 2. Arquitetura da Aplicação

Adotaremos a Clean Architecture, separando bem as responsabilidades e tornando o sistema mais modular, testável e flexível.

**Camadas:**

- **Entities (Entidades):** Regras de negócio de mais alto nível, independentes de frameworks.
- **Use Cases (Casos de Uso):** Lógica de aplicação, contendo operações específicas da aplicação.
- **Interface Adapters (Adaptadores):** Traduzem dados entre as camadas internas e externas (Views, Serializers, Repositórios).
- **Frameworks e Drivers:** Detalhes externos como Django, Docker, banco de dados, Once UI.

Estrutura de diretórios:

```bash
project/
│
├── entities/                    # Entidades
│   ├── user.py                  # Entidade Usuário
│   ├── category.py              # Entidade Categoria
│   ├── poll.py                  # Entidade Enquete
│   └── question.py              # Entidade Pergunta
│
├── use_cases/                   # Casos de Uso
│   ├── create_poll.py           # Criar Enquete
│   ├── update_poll.py           # Atualizar Enquete
│   ├── delete_poll.py           # Deletar Enquete
│   └── list_polls.py            # Listar Enquetes
│
├── adapters/                    # Adaptadores
│   ├── repositories/            # Repositórios
│   │   └── poll_repository.py   # Repositório de Enquetes
│   └── views/                   # Views Django
│       └── poll_view.py         # View de Enquetes
│
├── frameworks/                  # Frameworks externos
│   ├── django_app/              # Configuração do Django
│   ├── docker/                  # Configuração do Docker
│   └── once_ui/                 # Integração com Once UI
│
└── main.py                      # Ponto de entrada
```

## 3. Entidades

**Usuário:** Representa quem cria e gerencia enquetes.

- `id`: Identificador único.
- `username`: Nome de usuário.
- `email`: Email do usuário.
- `password`: Senha.

**Categoria:** Agrupa enquetes em temas.

- `id`: Identificador único.
- `name`: Nome da categoria.

**Enquete:** Conjunto de perguntas sobre um tema.

- `id`: Identificador único.
- `title`: Título da enquete.
- `category_id`: Categoria associada.
- `user_id`: Criador da enquete.

**Pergunta:** Parte de uma enquete.

- `id`: Identificador único.
- `poll_id`: Enquete associada.
- `text`: Texto da pergunta.

**Opção:** Respostas possíveis para uma pergunta.

- `id`: Identificador único.
- `question_id`: Pergunta associada.
- `text`: Texto da opção.
- `votes`: Número de votos.

## 4. Casos de Uso

**Enquetes:**

- `create_poll(title, category_id, user_id)`: Cria uma nova enquete.
- `update_poll(poll_id, title, category_id)`: Atualiza uma enquete existente.
- `delete_poll(poll_id)`: Remove uma enquete.
- `list_polls(category_id)`: Lista enquetes de uma categoria.

**Perguntas:**

- `add_question(poll_id, text)`: Adiciona uma pergunta.
- `update_question(question_id, text)`: Atualiza uma pergunta.
- `delete_question(question_id)`: Remove uma pergunta.

**Opções:**

- `add_option(question_id, text)`: Adiciona uma opção.
- `vote_option(option_id)`: Vota em uma opção.

## 5. Docker

Configuraremos Docker para rodar o Django e o banco de dados PostgreSQL em containers separados.

**docker-compose.yml:**

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: polls
```

## 6. Once UI

Once UI será usado para criar uma interface leve e moderna para a API. Vamos integrar através de componentes reutilizáveis.

## 7. DDD (Domain-Driven Design)

No DDD, focamos na modelagem do domínio da aplicação:

- **Agregados:** Enquete como raiz, contendo perguntas e opções.
- **Entidades:** Usuário, Categoria, Enquete, Pergunta, Opção.
- **Repositórios:** Abstração da persistência dos dados.
- **Serviços:** Implementação dos casos de uso.

Esse roteiro cobre a base para começar a construção do projeto. Podemos detalhar mais qualquer parte se precisar!
