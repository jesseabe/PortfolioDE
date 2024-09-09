import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
from modules.db_connection import DatabaseConnection
from contracts.contrato_vendas import MetricasVendasBase, MetricasVendasOut

def extrai_dados_vendas(dir_arquivo: str) -> pd.DataFrame:
    pass

@pa.check_output(MetricasVendasOut, lazy=True)
def transforma_dados_vendas(df: pd.DataFrame) -> pd.DataFrame:
    pass

def carrega_dados_vendas(df: pd.DataFrame) -> None:
    pass