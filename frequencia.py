import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_frequencia.csv')

# Exemplo: contar frequências da coluna 'categoria'
contagem = df['tipo_atendimento'].value_counts()

# Criar o gráfico
plt.figure(figsize=(8, 5))
contagem.plot(kind='bar', color='skyblue')
plt.title('Gráfico de Frequência')
plt.xlabel('tipo atendimento')
plt.ylabel('id chamado')
plt.tight_layout()
plt.show()