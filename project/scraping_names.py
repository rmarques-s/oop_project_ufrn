import requests
import pandas as pd
import matplotlib.pyplot as plt

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

    # Salva o dataframe em um arquivo CSV
    df.to_csv("project/dados.xlsx", index=False)

    # Salva o dataframe em um arquivo TXT
    with open("project/dados.txt", "w") as f:
        for row in df.itertuples(index=False):
            nome = str(row[0]).ljust(15)  # 15 é o comprimento máximo para a coluna "nome"
            ranking = str(row[1]).ljust(8)  # 8 é o comprimento máximo para a coluna "ranking"
            frequencia = str(row[2]).ljust(12)  # 12 é o comprimento máximo para a coluna "frequencia"
            f.write(nome + ranking + frequencia + '\n')

    # Imprime o dataframe
    print(df)

     # Gera um gráfico de barras da frequência dos nomes
    plt.bar(df["nome"], df["frequencia"])
    plt.xlabel("Nomes")
    plt.ylabel("Frequência")
    plt.title("Frequência dos Nomes")
    plt.xticks(rotation=90)  # Rotaciona os nomes do eixo x para facilitar a leitura

    # Exibe o gráfico
    plt.show()
    plt.savefig('project/')
    
else:
    # Imprime uma mensagem de erro
    print("Erro ao acessar a API:", response.status_code)