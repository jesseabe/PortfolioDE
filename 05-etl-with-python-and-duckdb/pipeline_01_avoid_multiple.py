import os
import gdown
import duckdb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime
# Carrega as variáveis de ambiente
load_dotenv()

def conectar_banco():
    """Conecta ao banco de dados DuckDB; cria o banco se não existir."""
    return duckdb.connect(database='duckdb.db', read_only=False)

def inicializar_tabela(con):
    """Cria a tabela se ela não existir."""
    con.execute("""
        CREATE TABLE IF NOT EXISTS historico_arquivos (
            nome_arquivo VARCHAR,
            horario_processamento TIMESTAMP
        )
    """)

def registrar_arquivo(con, nome_arquivo):
    """Registra um novo arquivo no banco de dados com o horário atual."""
    con.execute("""
        INSERT INTO historico_arquivos (nome_arquivo, horario_processamento)
        VALUES (?, ?)
    """, (nome_arquivo, datetime.now()))

def arquivos_processados(con):
    """Retorna um set com os nomes de todos os arquivos já processados."""
    return set(row[0] for row in con.execute("SELECT nome_arquivo FROM historico_arquivos").fetchall())

# Função para baixar uma pasta do Google Drive
def baixar_pasta_google_drive(url_pasta, diretorio_local):
    os.makedirs(diretorio_local, exist_ok=True)
    gdown.download_folder(url_pasta, output=diretorio_local, quiet=False, use_cookies=False)

# Função para listar arquivos CSV no diretório especificado
def listar_arquivos_csv(diretorio):
    arquivos_csv = []
    todos_os_arquivos = os.listdir(diretorio)
    for arquivo in todos_os_arquivos:
        if arquivo.endswith(".csv"):
            caminho_completo = os.path.join(diretorio, arquivo)
            arquivos_csv.append(caminho_completo)
    return arquivos_csv

# Função para ler um arquivo CSV e retornar um DataFrame
def ler_csv(caminho_do_arquivo):
    return duckdb.read_csv(caminho_do_arquivo)

# Função para adicionar uma coluna de total de vendas
def transformar(df):
    # Executa a consulta SQL que inclui a nova coluna, operando sobre a tabela virtual
    df_transformado = duckdb.sql("SELECT *, quantidade * valor AS total_vendas FROM df").df()
    # Remove o registro da tabela virtual para limpeza
    print(df_transformado)
    return df_transformado

# Função para converter o Duckdb em Pandas e salvar o DataFrame no PostgreSQL
def salvar_no_postgres(df_duckdb, tabela):
    DATABASE_URL = os.getenv("DATABASE_URL")  # Ex: 'postgresql://user:password@localhost:5432/database_name'
    engine = create_engine(DATABASE_URL)
    # Salvar o DataFrame no PostgreSQL
    df_duckdb.to_sql(tabela, con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    url_pasta = 'https://drive.google.com/drive/folders/1maqV7E3NRlHp12CsI4dvrCFYwYi7BAAf'
    diretorio_local = './pasta_gdown'

    # baixar_pasta_google_drive(url_pasta, diretorio_local)
    arquivos_csv = listar_arquivos_csv(diretorio_local)
    con = conectar_banco()
    inicializar_tabela(con)
    processados = arquivos_processados(con)
    for caminho_do_arquivo in arquivos_csv:
        nome_arquivo = os.path.basename(caminho_do_arquivo)
        if nome_arquivo not in processados:
            df = ler_csv(caminho_do_arquivo)
            df_transformado = transformar(df)
            salvar_no_postgres(df_transformado, "vendas_calculado")
            registrar_arquivo(con, nome_arquivo)
            print(f"Arquivo {nome_arquivo} processado e salvo.")
        else:
            print(f"Arquivo {nome_arquivo} já foi processado anteriormente.")