import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
from modules.db_connection import DatabaseConnection
from contracts.contrato_estoque import MetricasEstoqueBase, MetricasEstoqueOut

def extrai_dados_estoque(dir_arquivo: str) -> pd.DataFrame:
    pass

@pa.check_output(MetricasEstoqueOut, lazy=True)
def transforma_dados_estoque(df: pd.DataFrame) -> pd.DataFrame:
    pass

