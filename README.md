# project-biblioteKA

O BiblioteKA é um projeto voltado para livrarias. Em sua primeira versão, contamos com um sistema fechado no qual todo o controle é do administrador e dos colaboradores. Somente clientes físicos têm acesso ao site, devido ao cadastro presencial autorizado pelo administrador.
Nessa aplicação, os estudantes podem seguir os livros que desejam ler futuramente, listar todos os livros da livraria e solicitar empréstimo de livros. Dessa forma, é possível ter acesso ao livro já com uma data pré-determinada de devolução de 7 dias.
Os colaboradores são criados exclusivamente pelo administrador, que tem acesso total à aplicação. Com a função de colaborador, podem criar usuários, cadastrar livros, editá-los e excluí-los. Também têm acesso à rota de empréstimo, onde inserem as informações do cliente no sistema.
Link da doc: http://127.0.0.1:8000/api/docs/swagger-ui/#

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
