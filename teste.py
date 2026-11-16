import matplotlib.pyplot as plt
import pandas as pd

# Carregar o arquivo
df = pd.read_csv('dados/dados_distribuicao.csv')  # ou 'dados/dados_barras.csv'

# Imprime o nome exato das colunas no terminal
print("Colunas encontradas:", df.columns)
