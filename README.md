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
Host: ec2-44-194-117-205.compute-1.amazonaws.com
Database: d93kj2k0kc6g14
User: suqwthdqzsxjvb
Port: 5432
Password: a19005e0d0b7ca6db28a1892165b38b974089294dea8937b1411cc250b6633f9

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
