import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_barras.csv')

plt.figure(figsize=(8, 5))
plt.bar(df['categoria'], df['vendas_medias'], color='orange')
plt.title('Gráfico de Barras')
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.tight_layout()
plt.show()