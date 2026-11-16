import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Carregar os dados
df = pd.read_csv('dados/dados_regressao.csv')

plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='renda_mensal', y='gasto_mensal', color='green')
plt.title('Gráfico de Regressão')
plt.xlabel('renda_mensal')
plt.ylabel('gasto_mensal')
plt.tight_layout()
plt.show()