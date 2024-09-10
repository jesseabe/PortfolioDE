import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from contracts.contrato_compras import MetricasComprasBase, MetricasComprasOut

def extrai_dados_compras(dir_arquivo: str) -> pd.DataFrame:
    renomeia_colunas = {
        'Doc.compra': 'Doc_compras',
        'Data': 'Data',
        'Nome do fornecedor': 'Fornecedor',
        'ID do material': 'ID_material',
        'Descricao do material': 'Material_desc',
        'Quantidade': 'Quantidade',
        'UMP': 'UMB',
        'Montante': 'Montante',
        'Moeda': 'Moeda',
        'Taxa cambio':'Taxa_Cambio' 
    }
    df = le_arquivo_xlsx(dir_arquivo, renomeia_colunas)
    try:
        df = MetricasComprasBase.validate(df, lazy=True)
        return df
    except pa.errors.SchemaError as exc:
        print("Erro ao validar os dados")
        print(exc)
    return pd.DataFrame()


@pa.check_output(MetricasComprasOut, lazy=True)
def transforma_dados_compras(df: pd.DataFrame) -> pd.DataFrame:
    df_transformado = df.copy()
    print(f'Base Compras > Total de Linhas no df depois de copiar:', df_transformado['ID_material'].count())
    # Convert Taxa_Cambio to float after replacing ',' with '.'
    df_transformado['Taxa_Cambio'] = df_transformado['Taxa_Cambio'].str.replace(',', '.').astype(float)
    # Fillna only for non-numeric columns to avoid schema issues
    for col in df_transformado.select_dtypes(include=['object']).columns:
        df_transformado[col] = df_transformado[col].fillna("n/a")
    print(f'Base Compras > Total de Linhas no df depois do tratamento:', df_transformado['ID_material'].count()) 
    return df_transformado


def carrega_dados_compras(df, table_name, schema='public'):
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
            Doc_compras VARCHAR, 
            Data DATE,
            Fornecedor VARCHAR,
            ID_material INT,
            Material_desc VARCHAR,
            Quantidade FLOAT,
            UMB VARCHAR,
            Montante FLOAT,
            Moeda VARCHAR,
            Taxa_Cambio FLOAT
        );
        """
        cursor.execute(create_table_sql)
        connect.commit()

        # Inserir dados na tabela
        insert_sql = f"""
        INSERT INTO {schema}.{table_name} (Doc_compras, Data, Fornecedor, ID_material, Material_desc, Quantidade, UMB, Montante, Moeda, Taxa_Cambio) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        ON CONFLICT (id) DO NOTHING;
        """

        
        for i, row in df.iterrows():
            cursor.execute(
                insert_sql,
                (row['Doc_compras'], row['Data'], row['Fornecedor'], row['ID_material'], row['Material_desc'], row['Quantidade'], row['UMB'], row['Montante'], row['Moeda'], row['Taxa_Cambio'])
            )
        connect.commit()

        print("Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while interacting with PostgreSQL", error)

    finally:
        if connect:
            cursor.close()
            connect.close()
