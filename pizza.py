import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_pizza.csv')

plt.figure(figsize=(6, 6))
plt.pie(
    df['faturamento'],
    labels=df['canal_venda'],
    autopct='%1.1f%%',
    startangle=140,
)
plt.title('Gráfico de Pizza')
plt.tight_layout()
plt.show()