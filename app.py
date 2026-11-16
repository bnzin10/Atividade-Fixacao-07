import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# -----------------------------------------------------------------------------
# 1. Configuração da página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard - Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded" # Permite recolher/expandir o sidebar
)

# -----------------------------------------------------------------------------
# 2. Sidebar com as informações do aluno
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("👤 Informações do Aluno")
    st.markdown("---")
    st.markdown("**Nome:** Seu Nome Completo")
    st.markdown("**Número da Chamada:** 12")
    st.markdown("**Turma:** 3º Ano B / Turma X")
    st.markdown("---")
    st.info("💡 Clique no ícone '<' no topo para recolher esta barra lateral.")

# -----------------------------------------------------------------------------
# 3. Título do Dashboard
# -----------------------------------------------------------------------------
st.title("📊 Dashboard Analítico - Atividade 06")
st.markdown("Visualização integrada dos gráficos gerados e suas respectivas análises de dados.")
st.markdown("---")

# -----------------------------------------------------------------------------
# 4. Geração de gráficos de exemplo 
# -----------------------------------------------------------------------------

# --- GRÁFICO 1: Barras ---

@st.cache_data
def carregar_dados_barras():
    return pd.read_csv('dados/dados_barras.csv')

try:
    df_barras = carregar_dados_barras()
    
    # Criando a figura do seu gráfico
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.bar(df_barras['categoria'], df_barras['vendas_medias'], color='orange')
    ax1.set_title('Gráfico de Barras')
    ax1.set_xlabel('Categoria')
    ax1.set_ylabel('Valor')
    plt.tight_layout()
    
    analise_g1 = "A categoria com maior média de vendas se destaca visualmente, permitindo comparar o desempenho entre os diferentes segmentos do conjunto de dados."
except Exception as e:
    # Caso o arquivo não seja encontrado, exibe um alerta no dashboard
    fig1 = None
    analise_g1 = f"Erro ao carregar 'dados/dados_barras.csv': {e}"
    
    
# --- GRÁFICO 2: Boxplot ---
    
@st.cache_data
def carregar_dados_boxplot():
    return pd.read_csv('dados/dados_boxplot.csv')

try:
    df_boxplot = carregar_dados_boxplot()
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df_boxplot, y='salario', x='departamento', ax=ax2)
    ax2.set_title('Gráfico Boxplot - Salários por Departamento')
    ax2.set_xlabel('Departamento')
    ax2.set_ylabel('Salário')
    plt.tight_layout()
    analise_g2 = "O boxplot permite avaliar a distribuição, a mediana e a presença de outliers salariais em cada departamento."
except Exception as e:
    fig2 = None
    analise_g2 = f"Erro ao carregar 'dados/dados_boxplot.csv': {e}"
    

# --- GRÁFICO 3: Dispersão ---

@st.cache_data
def carregar_dados_dispersao():
    return pd.read_csv('dados/dados_dispersao.csv')

try:
    df_dispersao = carregar_dados_dispersao()
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.scatter(df_dispersao['altura_cm'], df_dispersao['peso_kg'], color='purple', alpha=0.7)
    ax3.set_title('Gráfico de Dispersão - Altura x Peso')
    ax3.set_xlabel('Altura em centímetros')
    ax3.set_ylabel('Peso KG')
    ax3.grid(True)
    plt.tight_layout()
    analise_g3 = "O gráfico de dispersão ilustra a relação bivariada entre altura e peso, evidenciando tendências gerais na amostra."
except Exception as e:
    fig3 = None
    analise_g3 = f"Erro ao carregar 'dados/dados_dispersao.csv': {e}"
    

# --- GRÁFICO 4: Distribuição / Histograma ---

@st.cache_data
def carregar_dados_distribuicao():
    return pd.read_csv('dados/dados_distribuicao.csv')

try:
    df_distribuicao = carregar_dados_distribuicao()
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.histplot(df_distribuicao['cliente_id'], kde=True, color='teal', ax=ax4)
    ax4.set_title('Gráfico de Distribuição / Histograma')
    ax4.set_xlabel('Cliente')
    ax4.set_ylabel('Idade')
    plt.tight_layout()
    analise_g4 = "O histograma combinado com a curva KDE permite visualizar a frequência e a densidade de distribuição dos dados coletados."
except Exception as e:
    fig4 = None
    analise_g4 = f"Erro ao carregar 'dados/dados_distribuicao.csv': {e}"
    
    
# --- GRÁFICO 5: Frequência ---

@st.cache_data
def carregar_dados_frequencia():
    return pd.read_csv('dados/dados_frequencia.csv')

try:
    df_frequencia = carregar_dados_frequencia()
    contagem = df_frequencia['tipo_atendimento'].value_counts()
    
    fig5, ax5 = plt.subplots(figsize=(8, 5))
    contagem.plot(kind='bar', color='skyblue', ax=ax5)
    ax5.set_title('Gráfico de Frequência - Tipos de Atendimento')
    ax5.set_xlabel('Tipo Atendimento')
    ax5.set_ylabel('Quantidade / ID Chamado')
    plt.tight_layout()
    analise_g5 = "O gráfico de barras de frequência evidencia quais tipos de atendimento possuem maior volume de registros no dataset."
except Exception as e:
    fig5 = None
    analise_g5 = f"Erro ao carregar 'dados/dados_frequencia.csv': {e}"
    
# --- GRÁFico 6: Heatmap / Mapa de Calor ---

@st.cache_data
def carregar_dados_heatmap():
    return pd.read_csv('dados/dados_heatmap.csv')

try:
    df_heatmap = carregar_dados_heatmap()
    df_pivot = df_heatmap.pivot(
        index='horario', columns='dia_semana', values='movimento_clientes'
    )
    
    fig6, ax6 = plt.subplots(figsize=(8, 5))
    sns.heatmap(
        df_pivot,
        annot=True,
        fmt='d',
        cmap='YlGnBu',
        linewidths=0.5,
        ax=ax6
    )
    ax6.set_title('Mapa de Calor - Movimento de Clientes')
    ax6.set_xlabel('Dia da Semana')
    ax6.set_ylabel('Horário')
    plt.tight_layout()
    analise_g6 = "O mapa de calor evidencia visualmente os horários e dias da semana com maior intensidade no fluxo de clientes."
except Exception as e:
    fig6 = None
    analise_g6 = f"Erro ao carregar 'dados/dados_heatmap.csv': {e}"
    
    
# --- GRÁFICO 7: Linhas ---

@st.cache_data
def carregar_dados_linhas():
    return pd.read_csv('dados/dados_linhas.csv')

try:
    df_linhas = carregar_dados_linhas()
    fig7, ax7 = plt.subplots(figsize=(8, 5))
    ax7.plot(df_linhas['data'], df_linhas['vendas'], marker='o', linestyle='-', color='b')
    # Otimizando a exibição de ticks no Streamlit
    if len(df_linhas) > 10:
        ax7.set_xticks(df_linhas['data'][::10])
    ax7.tick_params(axis='x', rotation=45)
    ax7.set_title('Gráfico de Linhas - Vendas ao Longo do Tempo')
    ax7.set_xlabel('Data')
    ax7.set_ylabel('Vendas')
    ax7.grid(True)
    plt.tight_layout()
    analise_g7 = "O gráfico de linhas demonstra a evolução temporal das vendas, facilitando a identificação de picos, quedas e tendências."
except Exception as e:
    fig7 = None
    analise_g7 = f"Erro ao carregar 'dados/dados_linhas.csv': {e}"
    

# --- GRÁFICO 8: Pizza  ---

@st.cache_data
def carregar_dados_pizza():
    return pd.read_csv('dados/dados_pizza.csv')

try:
    df_pizza = carregar_dados_pizza()
    fig8, ax8 = plt.subplots(figsize=(8, 5))
    ax8.pie(
        df_pizza['faturamento'],
        labels=df_pizza['canal_venda'],
        autopct='%1.1f%%',
        startangle=140
    )
    ax8.set_title('Gráfico de Pizza - Faturamento por Canal de Venda')
    plt.tight_layout()
    analise_g8 = "O gráfico de pizza ilustra a participação percentual de cada canal de venda no faturamento total da empresa."
except Exception as e:
    fig8 = None
    analise_g8 = f"Erro ao carregar 'dados/dados_pizza.csv': {e}"
    

# --- GRÁFICO 9: Regressão ---

@st.cache_data
def carregar_dados_regressao():
    return pd.read_csv('dados/dados_regressao.csv')

try:
    df_regressao = carregar_dados_regressao()
    fig9, ax9 = plt.subplots(figsize=(8, 5))
    sns.regplot(data=df_regressao, x='renda_mensal', y='gasto_mensal', color='green', ax=ax9)
    ax9.set_title('Gráfico de Regressão - Renda x Gasto Mensal')
    ax9.set_xlabel('Renda Mensal')
    ax9.set_ylabel('Gasto Mensal')
    plt.tight_layout()
    analise_g9 = "O gráfico de regressão exibe a linha de tendência estatística entre a renda mensal e o gasto mensal, mostrando o comportamento da relação."
except Exception as e:
    fig9 = None
    analise_g9 = f"Erro ao carregar 'dados/dados_regressao.csv': {e}"
    


graficos = {
    1: {"titulo": "Gráfico 1: Vendas Médias", "fig": fig1, "analise": analise_g1},
    2: {"titulo": "Gráfico 2: Salário por Departamento", "fig": fig2, "analise": analise_g2},
    3: {"titulo": "Gráfico 3: Altura vs Peso", "fig": fig3, "analise": analise_g3},
    4: {"titulo": "Gráfico 4: Distribuição de Clientes", "fig": fig4, "analise": analise_g4},
    5: {"titulo": "Gráfico 5: Frequência de Atendimentos", "fig": fig5, "analise": analise_g5},
    6: {"titulo": "Gráfico 6: Mapa de Calor (Movimento)", "fig": fig6, "analise": analise_g6},
    7: {"titulo": "Gráfico 7: Evolução de Vendas (Linhas)", "fig": fig7, "analise": analise_g7},
    8: {"titulo": "Gráfico 8: Faturamento por Canal (Pizza)", "fig": fig8, "analise": analise_g8},
    9: {"titulo": "Gráfico 9: Regressão (Renda x Gasto)", "fig": fig9, "analise": analise_g9}
}

# -----------------------------------------------------------------------------
# 6. Renderização em Grid (Três a Três)
# -----------------------------------------------------------------------------

def renderizar_trinca(ids_graficos):
    cols = st.columns(3)
    for index, g_id in enumerate(ids_graficos):
        if g_id in graficos:
            item = graficos[g_id]
            with cols[index]:
                st.subheader(item["titulo"])
                if item["fig"] is not None:
                    st.pyplot(item["fig"])
                else:
                    st.error("Figura não disponível.")
                
                # Análise logo abaixo do gráfico
                st.info(f"📝 **Análise:** {item['analise']}")

st.markdown("### 🔹 Primeira Trinca de Gráficos")
renderizar_trinca([1, 2, 3])

st.markdown("---")

st.markdown("### 🔹 Segunda Trinca de Gráficos")
renderizar_trinca([4, 5, 6])

st.markdown("---")

st.markdown("### 🔹 Terceira Trinca de Gráficos")
renderizar_trinca([7, 8, 9])