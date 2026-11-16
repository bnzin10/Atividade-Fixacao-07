import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_dispersao.csv')

plt.figure(figsize=(8, 5))
plt.scatter(df['altura_cm'], df['peso_kg'], color='purple', alpha=0.7)
plt.title('Gráfico de Dispersão')
plt.xlabel('Altura em centímetros')
plt.ylabel('Peso KG')
plt.grid(True)
plt.tight_layout()
plt.show()