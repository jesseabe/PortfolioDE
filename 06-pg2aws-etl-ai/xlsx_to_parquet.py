import pandas as pd
import os
import openpyxl
import csv
import duckdb

# Utilizando Pandas
def xlsx_to_parquet(caminho_xlsx, caminho_para_salvar=None):
    try:
        # Lendo o arquivo Excel
        df = pd.read_excel(caminho_xlsx)
        
        # Se o caminho para salvar não for especificado, usa o mesmo nome do arquivo original
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_xlsx))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"
        
        # Convertendo para Parquet
        df.to_parquet(caminho_para_salvar, index=False, encoding='utf-8')
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")


#Utilizando Duckdb
def xlsx_to_csv_duckdb(caminho_xlsx, caminho_para_salvar=None):
    try:
        # Se o caminho para salvar não for especificado, cria com o mesmo nome
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_xlsx))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"

        # Usando DuckDB para ler o arquivo Excel e converter para CSV
        duckdb.query(f"INSTALL 'excel'; LOAD 'excel';")  # Instala e carrega o módulo para XLSX
        df = duckdb.query(f"SELECT * FROM read_excel('{caminho_xlsx}')").df()
        
        # Salvar o DataFrame em CSV
        df.to_parquet(caminho_para_salvar, index=False, encoding='utf-8')
        
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")