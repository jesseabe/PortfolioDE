import pandas as pd
import os
import openpyxl
import csv
import duckdb

# Utilizando Pandas
def parquet_to_csv(caminho_parquet, caminho_para_salvar=None):
    try:
        # Lendo o arquivo Excel
        df = pd.read_parquet(caminho_parquet)
        
        # Se o caminho para salvar não for especificado, usa o mesmo nome do arquivo original
        if caminho_para_salvar is None:
            nome_arquivo = os.path.splitext(os.path.basename(caminho_parquet))[0]
            caminho_para_salvar = f"{nome_arquivo}.csv"
        
        # Convertendo para CSV
        df.to_csv(caminho_para_salvar, index=False, encoding='utf-8')
        print(f"Arquivo convertido e salvo em: {caminho_para_salvar}")
    
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")