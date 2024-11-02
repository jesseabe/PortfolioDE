import streamlit as st
import pandas as pd
import sqlite3

# Conecte-se ao banco de dados SQLite
con = sqlite3.connect('data/dre.db')

# Leia uma tabela específica do banco de dados
df = pd.read_sql('SELECT * FROM dre', con)

# Feche a conexão
con.close()

#Título do Dashboard
st.title("Apresentação de Resultados da XJEX")

#Título da tabela
st.write("Cabeçalho dos dados")
st.write(df.head())

import streamlit as st

RECEITA_BRUTA = df["Receita Bruta"].sum()
IMPOSTOS = df["Impostos"].sum()
RECEITA_LIQUIDA = df["Receita Líquida"].sum()
CMV = df["CMV"].sum()
LUCRO_BRUTO = df["Lucro Bruto"].sum()
DESPESA_OPERACIONAL = df["Despesa Operacional"].sum()
LUCRO_LÍQUIDO = df["Lucro Líquido"].sum()

st.write(f'RECEITA BRUTA: {round(RECEITA_BRUTA, 2)}')
st.write(f'IMPOSTOS: {round(IMPOSTOS, 2)}')
st.write(f'RECEITA LÍQUIDA: {round(RECEITA_LIQUIDA,2)}')
st.write(f'CMV: {round(CMV,2)}')
st.write(f'LUCRO BRUTO: {round(LUCRO_BRUTO,2)}')
st.write(f'DESPESA OPERACIONAL: {round(DESPESA_OPERACIONAL,2)}')
st.write(f'LUCRO LÍQUIDO: {round(LUCRO_LÍQUIDO,2)}')