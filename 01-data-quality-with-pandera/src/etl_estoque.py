import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from contracts.contrato_estoque import MetricasEstoqueBase, MetricasEstoqueOut

def extrai_dados_estoque(dir_arquivo: str) -> pd.DataFrame:
    renomeia_colunas = {
        'ID do material': 'ID_Material',
        'data': 'Data',
        'Valor do estoque': 'Valor',
        'Quantidade do estoque': 'Quantidade',
        'UMB': 'UMB'
    }
    df = le_arquivo_xlsx(dir_arquivo, renomeia_colunas)
    try:
        df = MetricasEstoqueBase.validate(df, lazy=True)
        return df
    except pa.errors.SchemaError as exc:
        print("Erro ao validar os dados")
        print(exc)
    return pd.DataFrame()


@pa.check_output(MetricasEstoqueOut, lazy=True)
def transforma_dados_estoque(df: pd.DataFrame) -> pd.DataFrame:
    df_transformado = df.copy()
    print(df_transformado.head())
    print(f'Base Estoque > Total de Linhas no df depois de copiar:', df_transformado['ID_Material'].count())
    # Fillna only for non-numeric columns to avoid schema issues
    for col in df_transformado.select_dtypes(include=['object']).columns:
        df_transformado[col] = df_transformado[col].fillna("n/a")
    print(f'Base Estoque > Total de Linhas no df depois do tratamento:', df_transformado['ID_Material'].count()) 
    print(df_transformado.head())
    return df_transformado


def carrega_dados_estoque(df, table_name, schema='public'):
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
            ID_Material INT, 
            Data DATE,
            Valor FLOAT,
            Quantidade FLOAT,
            UMB VARCHAR
        );
        """
        cursor.execute(create_table_sql)
        connect.commit()

        # Inserir dados na tabela
        insert_sql = f"""
        INSERT INTO {schema}.{table_name} (ID_Material, Data, Valor, Quantidade, UMB) 
        VALUES (%s, %s, %s, %s, %s) 
        ON CONFLICT (id) DO NOTHING;
        """

        
        for i, row in df.iterrows():
            cursor.execute(
                insert_sql,
                (row['ID_Material'], row['Data'], row['Valor'], row['Quantidade'], row['UMB'])
            )
        connect.commit()

        print("Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while interacting with PostgreSQL", error)

    finally:
        if connect:
            cursor.close()
            connect.close()

