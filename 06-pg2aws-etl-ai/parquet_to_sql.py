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
def csv_to_sql(parquet_file: str, table_name: str, if_exists: str = 'replace'):
    # Carrega o DataFrame do arquivo Parquet
    df = pd.read_parquet(parquet_file)

    # Cria o engine de conexão com o PostgreSQL
    engine = create_engine(database_url_postgres)
    
    try:
        # Envia o DataFrame para o PostgreSQL
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        print(f"Dados carregados com sucesso na tabela '{table_name}' do banco PostgreSQL.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")