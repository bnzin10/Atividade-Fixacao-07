import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Carregar os dados
df = pd.read_csv('dados/dados_boxplot.csv')

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, y='salario', x='departamento')
plt.title('Gráfico Boxplot')
plt.tight_layout()
plt.show()