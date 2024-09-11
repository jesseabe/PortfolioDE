import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
from psycopg2 import Error

def carrega_dados(df: pd.DataFrame, nome_da_tabela: str) -> None:
    load_dotenv(".env")

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    POSTGRES_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    engine = create_engine(POSTGRES_DATABASE_URL)

    try:
        df.to_sql(nome_da_tabela, engine, if_exists= "replace", index = False)
    except Exception as e:
        print(e)
    finally:
        # Libera os recursos do engine
        engine.dispose()


def connectpostgres():
    # Get environment variables
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    dbname = os.getenv("POSTGRES_DB")

    # Create connection
    connect = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        dbname=dbname
    )

    # Create a cursor object
    cursor = connect.cursor()
    connect.autocommit = True
    return cursor
