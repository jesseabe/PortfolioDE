import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco SQL
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela no pandas
df = pd.read_sql_query("SELECT * FROM cursos_ead", conn)  # Passa a conexão como segundo argumento

# Fechar a conexão 
conn.close()

# Título do dashboard
st.title('Painel de Inteligência Competitiva')

# Visualizando a tabela
st.write(df)


