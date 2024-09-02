# Pasta de arquivos docker 

Nessa pasta está o arquivo docker-compose.yml. 

Ele possui um postgres para execução do ambiente local. Por padrão ele roda com confiugrações padrão da imagem do Postgres:
Usuário e senha: postgres
Porta: 5432

Para rodar, navegue até o diretório  docker e rode o comando:

```bash
docker compose up -d
```