import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Carregar os dados
df = pd.read_csv('dados/dados_distribuicao.csv')

plt.figure(figsize=(8, 5))
sns.histplot(df['cliente_id'], kde=True, color='teal')
plt.title('Gráfico de Distribuição / Histograma')
plt.xlabel('Cliente')
plt.ylabel('Idade')
plt.tight_layout()
plt.show()