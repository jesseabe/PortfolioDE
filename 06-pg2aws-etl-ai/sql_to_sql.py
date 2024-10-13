import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(".env")

# Carrega as URLs dos bancos de dados a partir das variáveis de ambiente
database_url_postgres_source = os.getenv("DATABASE_URL_POSTGRES_SOURCE")
database_url_postgres_target = os.getenv("DATABASE_URL_POSTGRES_TARGET")

# Verifica se as URLs foram carregadas corretamente
if not database_url_postgres_source or not database_url_postgres_target:
    raise ValueError("As URLs dos bancos de dados não foram encontradas. Verifique o arquivo .env.")

def sql_to_sql(nome_tabela_postgres) -> None:
    try:
        # Cria a engine para o banco de dados de origem
        engine_source = create_engine(database_url_postgres_source)
        print("Conexão com o banco de dados de origem estabelecida.")

        # Monta a query SQL dinamicamente
        query = f"SELECT * FROM {nome_tabela_postgres}"
        print("Query gerada para leitura.")

        # Executa a query e carrega os dados em um DataFrame
        df = pd.read_sql(query, engine_source)
        print(f"Dados da tabela '{nome_tabela_postgres}' carregados.")

        # Cria a engine para o banco de dados de destino
        engine_target = create_engine(database_url_postgres_target)
        print("Conexão com o banco de dados de destino estabelecida.")

        # Salva o DataFrame no banco de dados de destino
        df.to_sql(nome_tabela_postgres, engine_target, if_exists='replace', index=False)
        print(f"Dados da tabela '{nome_tabela_postgres}' transferidos para o banco de dados de destino.")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    # Chama a função passando o nome da tabela
    sql_to_sql("vendas_calculado")
