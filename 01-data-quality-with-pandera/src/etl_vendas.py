import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from contracts.contrato_vendas import MetricasVendasBase, MetricasVendasOut

def extrai_dados_vendas(dir_arquivo: str) -> pd.DataFrame:
    renomeia_colunas = {
        'Data': 'Data',
        'ID do material': 'ID_Material',
        'Descricao do material': 'Material_desc',
        'Venda em reais': 'Faturamento'
    }
    df = le_arquivo_xlsx(dir_arquivo, renomeia_colunas)
    try:
        df = MetricasVendasBase.validate(df, lazy=True)
        return df
    except pa.errors.SchemaError as exc:
        print("Erro ao validar os dados")
        print(exc)
    return pd.DataFrame()


@pa.check_output(MetricasVendasOut, lazy=True)
def transforma_dados_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_transformado = df.copy()
    print(df_transformado.head())
    return df_transformado


def carrega_dados_vendas(df, table_name, schema='public'):
    load_dotenv(".env")
    """
    Insere dados de um DataFrame em uma tabela PostgreSQL.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem inseridos.
        table_name (str): Nome da tabela onde os dados serão inseridos.
        schema (str): Nome do schema onde a tabela está localizada. Padrão é 'public'.
    """
    try:
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

        # Criar a tabela se não existir
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {schema}.{table_name} (
            id SERIAL PRIMARY KEY,
            Data DATE,
            ID_Material INT, 
            Material_desc VARCHAR,
            Faturamento FLOAT
        );
        """
        cursor.execute(create_table_sql)
        connect.commit()

        # Inserir dados na tabela
        insert_sql = f"""
        INSERT INTO {schema}.{table_name} (Data, ID_Material, Material_desc, Faturamento) 
        VALUES (%s, %s, %s, %s) 
        ON CONFLICT (id) DO NOTHING;
        """

        
        for i, row in df.iterrows():
            cursor.execute(
                insert_sql,
                (row['Data'], row['ID_Material'], row['Material_desc'], row['Faturamento'])
            )
        connect.commit()

        print("Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while interacting with PostgreSQL", error)

    finally:
        if connect:
            cursor.close()
            connect.close()
