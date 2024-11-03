import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import matplotlib.pyplot as plt

# Conecte-se ao banco de dados SQLite
con = sqlite3.connect('data/dre.db')

# Leia uma tabela específica do banco de dados
df = pd.read_sql('SELECT * FROM dre', con)

# Feche a conexão
con.close()

#Título do Dashboard
st.title("Apresentação de Resultados")

# Calculando os valores
RECEITA_BRUTA = df["Receita Bruta"].sum() / 1_000
IMPOSTOS = df["Impostos"].sum() / 1_000
RECEITA_LIQUIDA = df["Receita Líquida"].sum() / 1_000
CMV = df["CMV"].sum() / 1_000
LUCRO_BRUTO = df["Lucro Bruto"].sum() / 1_000
DESPESA_OPERACIONAL = df["Despesa Operacional"].sum() / 1_000
LUCRO_LIQUIDO = df["Lucro Líquido"].sum() / 1_000

# Criando um DataFrame para exibir os dados como uma tabela
data = {
    "Descrição": [
        "Receita Bruta",
        "Impostos",
        "Receita Líquida",
        "CMV",
        "Lucro Bruto",
        "Despesa Operacional",
        "Lucro Líquido"
    ],
    "Valor (em milhares)": [
        RECEITA_BRUTA,
        IMPOSTOS,
        RECEITA_LIQUIDA,
        CMV,
        LUCRO_BRUTO,
        DESPESA_OPERACIONAL,
        LUCRO_LIQUIDO
    ]
}

# Convertendo para DataFrame
df_table = pd.DataFrame(data)

# Formatando os valores para duas casas decimais com separadores de milhar
df_table["Valor (em milhares)"] = df_table["Valor (em milhares)"].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Exibindo a tabela no Streamlit
st.table(df_table)


# Criando o gráfico de barras para Receita Líquida por Categoria
plt.figure(figsize=(10, 6))
plt.bar(df['Categoria'], df['Receita Líquida'], color='skyblue')
plt.title('Receita Líquida por Categoria')
plt.xlabel('Categorias')
plt.ylabel('Receita Líquida (em milhares)')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X para melhor visualização
st.pyplot(plt)
