import sys
import os


# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl_compras import extrai_dados_compras, transforma_dados_compras, carrega_dados_compras
#from etl_estoque import extrai_dados_estoque, transforma_dados_estoque
#from etl_vendas import extrai_dados_vendas, transforma_dados_vendas
#from modules.db_connection import carrega_dados

def run_etl_compras():
    dir_arquivo = "data/compras.xlsx"
    df = extrai_dados_compras(dir_arquivo)
    print("Dados de compras extraídos")
    if not df.empty:
        df_transformado = transforma_dados_compras(df)
        print("Dados de compras transformados")
        carrega_dados_compras(df_transformado, "compras")

# def run_etl_estoque():
#     dir_arquivo = "data/estoque.xlsx"
#     df = extrai_dados_estoque(dir_arquivo)
#     print("Dados de compras extraídos")
#     if not df.empty:
#         df_transformado = transforma_dados_estoque(df)
#         print("Dados de estoque transformados")
#         carrega_dados(df_transformado, 'estoque')

# def run_etl_vendas():
#     dir_arquivo = "data/vendas.xlsx"
#     df = extrai_dados_vendas(dir_arquivo)
#     print("Dados de vendas extraídos")
#     if not df.empty:
#         df_transformado = transforma_dados_vendas(df)
#         print("Dados de vendas transformados")
#         carrega_dados(df_transformado, 'vendas')

if __name__ == "__main__":
    run_etl_compras()
    print("Base de compras carregada com sucesso")
    #run_etl_estoque
    #print("Base de estoque carregada com sucesso")
    #run_etl_vendas
    #print("Base de vendas carregada com sucesso")