# project-biblioteKA

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
