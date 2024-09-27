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

Para rodar os testes automáticos execute:
```bash
pytest .
```

# Shell do Django

Esse template vem com  [Django Extensions](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html) instalado.
Então se recomenda usar. Para rodar sessão shell interativa

```bash
python manage.py shell_plus --print-sql
```

# Testes com Cobertura

Foi utilizado o [pytest-coverage](https://pytest-cov.readthedocs.io/en/latest/) que produz um relatório de cobertura.
Foi instalado no grupo de desenvolvimento.

```bash
poetry add -G dev pytest-cov
pytest --cov=base/
```

# Django Toolbar

# Usuário padrão

Nesse projeto o usuário foi customizado. Ele não tem username nem last_name como o usuário padrão do Django.
Ele usa o email como identificador único. O usuário se encontra na app base para que você possa acrescentar 
campos de acordo com sua necessidade.

## Configurações de instância

Para ler configurações de instânca, esse projeto usa a lib [python decouple](https://pypi.org/project/python-decouple/).
Ela é importada no arquivo settings.py

## Upload de arquivos

Projeto está configurado para gravar arquivos públicos e privados. Por isso, se usar ImageField ou FieldField,
o parâmetro "upload_to" precisa ter prefixo "public" para arquivos que sejam publicos e "private" para privados. 
Exemplos:
```python
from django.db import models


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='public/base/avatars/', blank=True, null=True)


class NotaFiscal(models.Model):
    arquivo = models.ImageField(upload_to='private/base/notas_fiscais/')
```