import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Carregar o ficheiro do heatmap
df = pd.read_csv('dados/dados_heatmap.csv')

# 2. Transformar os dados numa tabela pivô (matriz)
# Linhas = horário, Colunas = dia da semana, Valores = movimento de clientes
df_pivot = df.pivot(
    index='horario', columns='dia_semana', values='movimento_clientes'
)

# 3. Criar a figura do gráfico
plt.figure(figsize=(10, 6))

# 4. Gerar o mapa de calor
sns.heatmap(
    df_pivot,
    annot=True,  # Mostra os valores numéricos dentro dos quadrados
    fmt='d',  # Formata como número inteiro
    cmap='YlGnBu',  # Esquema de cores (amarelo, verde e azul)
    linewidths=0.5,  # Linhas finas a separar as células
)

# 5. Adicionar títulos e rótulos
plt.title('Mapa de Calor - Movimento de Clientes por Horário e Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Horário')
plt.tight_layout()
plt.show()