# Teste admissão empresa BR MED

Funcionalidades API:
 - **Buscar dados (5 cotações do dólar em relação ao Real, Euro e Iene ) na API vatcomply e inseri-los no banco de dados** 
 - **Plotar o gráfico inicial, com as 5 últimas cotações do Dólar em relação ao Real, Euro e Iene**
 - **Plotar gráfico com no máximo 5 cotações do Dólar em relação ao Real, Euro e Iene, considerando o intervalo de datas selecionadas**

## Stack

 - Django 4.0.4
 - Python 3.8.10
 - PostgreSql 13


## Informações Deploy

URL de acesso a aplicação hospedada no Heroku


Link Acesso Aplicação

``` Host
https://test-br-med.herokuapp.com/
```

Database

``` Database
Host: ec2-34-231-177-125.compute-1.amazonaws.com
Database: d94bkr682h2l3d
User: ojeiplazgwtvfz
Port: 5432
Password: 3d7f8a2625bf26a92121fb2dbcc0d8bae9b76e3a2f28edcd1e03fba7246f0534

```

## Endpoints Desenvolvidos

> Obter 5 cotações na API vatcomply e persisti-las no banco de dados

```plaintext
GET /apis/cotacao/seed
```

Exemplo da requisição:

```shell
curl "https://test-br-med.herokuapp.com/apis/cotacao/seed"
```

* obs: Execute esse endpoint PRIMEIRAMENTE para alimentar o banco de dados *

> Gerar gráfico com as cotações (apenas 5) mais recentes salvas no banco de dados.

```plaintext
GET /apis/cotacao/chart
```

Exemplo da requisição:

```shell
curl "https://test-br-med.herokuapp.com/apis/cotacao/chart"
```

> Gerar gráfico com as cotações (apenas 5) salvas no banco de dados, utilizando o intervalo de data selecionado pelo usuário.

```plaintext
POST /apis/cotacao/date
```

Exemplo da requisição:

```shell
curl -X POST "https://test-br-med.herokuapp.com/apis/cotacao/chart/date"
```

> Obter todas as cotações salvas no banco de dados

```plaintext
GET /apis/cotacao/getall
```

Exemplo da requisição:

```shell
curl "https://test-br-med.herokuapp.com/apis/cotacao/getall"
```
## Testes

Os testes foram executados com o comando:

```shell
Horuku run python3 manage.py test
```
