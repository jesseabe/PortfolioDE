import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(".env")

# Carrega a URL do banco de dados a partir das variáveis de ambiente

database_url_postgres = os.getenv("DATABASE_URL_POSTGRES")


# Verifica se a URL foi carregada corretamente
if not database_url_postgres:
    raise ValueError("A URL do banco de dados não foi encontrada. Verifique o arquivo .env.")


def sql_to_csv(nome_tabela_postgres) -> pd.DataFrame:
    try:
        engine_postgres = create_engine(database_url_postgres)
        print("engine criada")

        # Monta a query SQL dinamicamente
        query = f"SELECT * FROM {nome_tabela_postgres}"
        print("query salva")

        # Executa a query e carrega os dados em um DataFrame
        df = pd.read_sql(query, engine_postgres)
        print("query gerada")

        # Salva o DataFrame em um arquivo CSV
        df.to_csv(f"{nome_tabela_postgres}.csv", index=False)
        return df
    except Exception as e:
        print(f"Erro: {e}")



if __name__ == "__main__":
    # Chama a função passando o nome da tabela
    sql_to_csv("vendas_calculado")



