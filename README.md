# Teste admissão empresa BR MED

API endpoints desenvolvidos:
 - **Buscar dados (5 cotações do dólar em relação ao Real, Euro e Iene ) na API vatcomply e inseri-los no banco de dados** 
 - **Plotar o gráfico inicial, com as 5 últimas cotações do Dólar em relação ao Real, Euro e Iene**
 - **Plotar gráfico com no máximo 5 cotações do Dólar em relação ao Real, Euro e Iene, considerando o intervalo de datas selecionadas**

## Instalar e Executar

**1. Criar um ambiente virtual no cmd:**
    ```
    virtualenv 'nome_ambiente'
    ```

**2. Ativar ambiente virtual no cmd:**
 ```
 Windows - nome_ambiente/Scripts/activate
 Linux/Mac OS - source nome_ambiente/bin/activate
 ```
 
**3. Baixar o projeto:**
 ```
 git clone https://github.com/caio-cunha/br-med.git
 ```
 
**4. Instalar dependências (entrar na pasta brmed/br-med):**
 ```
 python3 -m pip install -r requirements.txt
 ```
 
**5. Testar a aplicação (entrar na pasta do app principal -brmed):**
 ```
 python3 manage.py runserver
 ```
 
**6. Executar os testes:**
 ```
 python3 manage.py test
 ```
