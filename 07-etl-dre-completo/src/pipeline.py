import pandas as pd
import duckdb

# Conecta ao DuckDB
conn = duckdb.connect()

# Registra o banco de dados SQLite no DuckDB e lê a tabela 'dre'
conn.execute("INSTALL sqlite;")  # Instala o suporte ao SQLite no DuckDB
conn.execute("LOAD sqlite;")     # Carrega o suporte ao SQLite

# Faz a leitura da tabela 'dre' dentro do arquivo SQLite
df = conn.execute("SELECT * FROM sqlite_scan('data/dre.db', 'dre')").df()

print(df.head())




