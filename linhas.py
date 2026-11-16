import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_linhas.csv')

plt.figure(figsize=(12, 6))
plt.plot(df['data'], df['vendas'], marker='o', linestyle='-', color='b')
plt.xticks(rotation=45, ha='right')
plt.xticks(df['data'][::10], rotation=45, ha='right') # -> Mostra apenas 1 rótulo a cada 10 linhas de dados (podes alterar o número 10)
plt.title('Gráfico de Linhas')
plt.xlabel('data')
plt.ylabel('vendas')
plt.grid(True)
plt.tight_layout()
plt.show()