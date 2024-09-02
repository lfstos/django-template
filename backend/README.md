# Backend Django

Nessa para se encontra os arquivos do projeto em Django.

Será usando o Poetry como gestor de pacotes.

Por isso, para instalar o projeto com a s dependências de desenvolvimento rode, dentro da pasta backend rode

```bash
poetry install with dev
```

Para para rodar seu servidor django ative o ambiente virtual:

```bash
poetry shell
```

Então rode

```bash
python mananage.py runserver
```

## Padrão de código

Para o backend esse projeto usa o flake8, com as seguintes customizações.

Tamanho de linha poder ter até 120 caracteres. Para ver o relatório do linter rode

```bash
flake8 .
```

# Usuário padrão

Nesse projeto o usuário foi customizado. Ele não tem username nem last_name como o usuário padrão do Django.
Ele usa o email como identificador único. O usuário se encontra na app base para que você possa acrescentar 
campos de acordo com sua necessidade.