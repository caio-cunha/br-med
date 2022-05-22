# Teste admissão empresa BR MED

API endpoints desenvolvidos:
 - **Buscar dados (5 cotações do dólar em relação ao Real, Euro e Iene ) na API vatcomply e inseri-los no banco de dados** 
 - **Plotar o gráfico inicial, com as 5 últimas cotações do Dólar em relação ao Real, Euro e Iene**
 - **Plotar gráfico com no máximo 5 cotações do Dólar em relação ao Real, Euro e Iene, considerando o intervalo de datas selecionadas**

## Endpoints Desenvolvidos

> Obter 5 cotações na API vatcomply e persisti-las no banco de dados

```plaintext
METHOD /apis/cotacao/seed
```

Example request:

```shell
curl "https://test-br-med.herokuapp.com/apis/cotacao/seed"
```

> Gerar gráfico com as últimas 5 cotações salvas no banco de dados.

```plaintext
METHOD /apis/cotacao/chart
```

Example request:

```shell
curl "https://test-br-med.herokuapp.com/apis/cotacao/chart"
```
