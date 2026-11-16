# Análise e Visualização de Dados em Python 📊

Este projeto consiste em um conjunto de scripts Python voltados para a exploração, análise estatística e visualização de dados utilizando diferentes tipos de gráficos. O objetivo é demonstrar como importar dados de arquivos CSV e transformá-los em visualizações claras e informativas.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **[Python](https://www.python.org/)** (versão 3.8 ou superior)
- **[Pandas](https://pandas.pydata.org/)**: Manipulação e leitura dos arquivos CSV.
- **[Matplotlib](https://matplotlib.org/)**: Criação de gráficos base e customização visual.
- **[Seaborn](https://seaborn.pydata.org/)**: Visualização de dados estatísticos de alto nível.

---

## 📂 Estrutura do Projeto

Os dados de entrada estão organizados em arquivos `.csv` específicos para cada tipo de gráfico:

- `dados_frequencia.csv`: Dados categóricos para análise de frequências.
- `dados_heatmap.csv`: Matriz de dados para correlação/mapas de calor.
- `dados_linhas.csv`: Séries temporais ou acompanhamento contínuo.
- `dados_pizza.csv`: Proporções e percentuais de partes em relação a um todo.
- `dados_regressao.csv`: Variáveis com relação de tendência/ajuste linear.
- `dados_barras.csv`: Comparação numérica entre categorias.
- `dados_boxplot.csv`: Análise de distribuição estatística e detecção de *outliers*.
- `dados_dispersao.csv`: Correlação entre duas variáveis contínuas (*Scatter Plot*).
- `dados_distribuicao.csv`: Distribuição de frequência contínua (Histograma/KDE).

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos e Instalação

Certifique-se de ter as dependências instaladas no seu ambiente. Caso não tenha, instale-as via terminal:

```bash
pip install pandas matplotlib seaborn
```

### 2. Configuração do Editor (Ex: VS Code)

Caso encontre o aviso de módulo não encontrado (`Import "matplotlib.pyplot" could not be resolved`), certifique-se de selecionar o interpretador Python correto:
1. Pressione `Ctrl + Shift + P` (no Windows/Linux) ou `Cmd + Shift + P` (no Mac).
2. Digite **Python: Select Interpreter**.
3. Escolha o ambiente onde os pacotes foram instalados.

### 3. Executando os Scripts

Você pode rodar cada script individualmente apontando para o seu respetivo arquivo CSV, ou carregar os dados em lote usando o Pandas.

Exemplo de execução via terminal:
```bash
python script_analise.py
```

---

## 📈 Gráficos Desenvolvidos

1. **Gráfico de Frequência:** Contagem de ocorrências por categoria.
2. **Heatmap (Mapa de Calor):** Matriz de correlação entre variáveis.
3. **Gráfico de Linhas:** Tendências e evolução de dados.
4. **Gráfico de Pizza:** Proporções relativas em formato percentual.
5. **Gráfico de Regressão:** Ajuste de linha de tendência sobre pontos de dispersão.
6. **Gráfico de Barras:** Comparação direta de valores entre grupos.
7. **Boxplot:** Resumo estatístico (Mínimo, Q1, Mediana, Q3, Máximo e Outliers).
8. **Gráfico de Dispersão:** Relação entre duas variáveis numéricas.
9. **Gráfico de Distribuição:** Histograma com estimativa de densidade suave (KDE).