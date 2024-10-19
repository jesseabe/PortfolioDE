import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import duckdb
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(".env")

# Carrega a URL do banco de dados a partir das variáveis de ambiente

database_url_postgres = os.getenv("DATABASE_URL_POSTGRES")

#Função utilizando Pandas 
def xlsx_to_sql(excel_file: str, table_name: str, if_exists: str = 'replace'):
    # Carrega o DataFrame do arquivo Excel
    df = pd.read_excel(excel_file)

    # Cria o engine de conexão com o PostgreSQL
    engine = create_engine(database_url_postgres)
    
    try:
        # Envia o DataFrame para o PostgreSQL
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        print(f"Dados carregados com sucesso na tabela '{table_name}' do banco PostgreSQL.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")



#Função utilizando Duckdb 
def xlsx_to_duckdb(excel_file: str, table_name: str, if_exists: str = 'replace'):
    # Carrega o DataFrame do arquivo Excel
    df = pd.read_excel(excel_file)

    # Conecta ao banco de dados DuckDB
    con = duckdb.connect(database_url_postgres)

    try:
        if if_exists == 'replace':
            # Remove a tabela existente, se houver
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
        elif if_exists == 'fail' and con.execute(f"SELECT * FROM information_schema.tables WHERE table_name = '{table_name}'").fetchone():
            raise ValueError(f"A tabela '{table_name}' já existe.")

        # Escreve os dados no DuckDB
        con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM df")
        print(f"Dados carregados com sucesso na tabela '{table_name}' do banco DuckDB.")
    
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
    
    finally:
        con.close()



if __name__ == "__main__":
    xlsx_to_sql('caminho/do/arquivo.xlsx', 'nome_da_tabela')
    xlsx_to_duckdb('caminho/do/arquivo.xlsx', 'nome_da_tabela')