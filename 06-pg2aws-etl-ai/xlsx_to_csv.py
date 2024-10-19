import pandas as pd
import os
import openpyxl
import csv
import os
from xlsx2csv import Xlsx2csv
import os
import duckdb

# Utilizando Pandas
def xlsx_to_csv(caminho_xlsx, caminho_para_salvar=None):
    try:
        # Lendo o arquivo Excel
        df = pd.read_excel(caminho_xlsx)
        
        # Se o caminho para salvar não for especificado, usa o mesmo nome do arquivo original
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_xlsx))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"
        
        # Convertendo para CSV
        df.to_csv(caminho_para_salvar, index=False, encoding='utf-8')
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")


# Utilizando openpyxl
def xlsx_to_csv_openpyxl(caminho_xlsx, caminho_para_salvar=None):
    try:
        # Carregar o arquivo Excel com openpyxl
        wb = openpyxl.load_workbook(caminho_xlsx)
        sheet = wb.active
        
        # Se o caminho para salvar não for especificado, cria com o mesmo nome
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_xlsx))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"

        # Abrir arquivo CSV e gravar nele
        with open(caminho_para_salvar, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in sheet.iter_rows(values_only=True):
                writer.writerow(row)
        
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")


#Utilizando xlsx2csv
def xlsx_to_csv_xlsx2csv(caminho_xlsx, caminho_para_salvar=None):
    try:
        # Se o caminho para salvar não for especificado, cria com o mesmo nome
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_xlsx))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"
        
        # Converter XLSX para CSV usando xlsx2csv
        Xlsx2csv(caminho_xlsx, outputencoding="utf-8").convert(caminho_para_salvar)
        
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
        df.to_csv(caminho_para_salvar, index=False, encoding='utf-8')
        
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")
