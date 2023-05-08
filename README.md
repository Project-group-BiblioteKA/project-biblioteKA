# project-biblioteKA

O BiblioteKA é um projeto voltado para bibliotecas. Em sua primeira versão, contamos com um sistema fechado no qual todo o controle é do administrador e dos colaboradores. Todos podem criar conta com suas devidas limitações.

Nessa aplicação, os estudantes podem seguir os livros que desejam ler futuramente, listar todos os livros da livraria e solicitar empréstimo de livros. Dessa forma, é possível ter acesso ao livro já com uma data pré-determinada de devolução de 7 dias.

Os colaboradores são criados exclusivamente pelo administrador, que tem acesso total à aplicação. Com a função de colaborador, podem <u>criar</u> usuários, <u>cadastrar</u> livros, <u>editá-los</u> e <u>excluí-los</u>. Também têm acesso à rota de empréstimo, onde inserem as informações do cliente no sistema.

Link da doc: http://127.0.0.1:8000/api/docs/swagger-ui/#

## Tecnologias

    - Python.
    - Django.
    - django_restframework.
    - psycopg2-binary.
    - djangorestframework-simplejwt.
    - postgree.
    - drf-spectacular.

## Sobre o time

Hugo Brito: https://www.linkedin.com/in/hugommbrito/

Matheus Henrique: https://www.linkedin.com/in/matheushgrohs/

Dionisio Benevides: https://www.linkedin.com/in/dionisiosantos/

Jozhué Beni: https://www.linkedin.com/in/jozhué-beni-f-n-b-mota-8584a5241/

## Instalação dos pacotes necessários

### Instalação do ambiente virtual (venv)

`python -m venv venv`

###### BASH

- Utilize o comando `source venv/Scripts/activate` caso o seu sistema operacional for **WINDOWS** para ativar o ambiente virtual.

- Utilize o comando `source venv/bin/activate` caso o seu sistema operacional for **LINUX** para ativar o ambiente virtual.

###### POWERSHELL

- Utilize o comando `.\venv\Scripts\activate` caso o seu sistema operacional for **WINDOWS** para ativar o ambiente virtual.

- Utilize o mesmo comando apresentado anteriormente no Bash, caso seja **LINUX**

### Instalação das dependências da aplicação

`pip install -r requirements.txt`

### Criação automática de um usuário Admin

Abra o terminal, e coloque o código:
`python manage.py create_admin_user`
