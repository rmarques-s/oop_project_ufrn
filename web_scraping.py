import requests
import pandas as pd

# Define a URL da API
url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"

# Faz uma requisição GET para a API
response = requests.get(url)

# Verifica se a requisição foi bem sucedida (status code 200)
if response.status_code == 200:
    # Converte a resposta em um objeto JSON
    data = response.json()

    # Cria um dataframe com os dados
    df = pd.DataFrame(data[0]["res"])

    # Seleciona apenas as colunas relevantes
    df = df[["nome", "ranking", "frequencia"]]

    # Ordena o dataframe pelo ranking
    df = df.sort_values("ranking")

    # Imprime o dataframe
    print(df)
else:
    # Imprime uma mensagem de erro
    print("Erro ao acessar a API:", response.status_code)
