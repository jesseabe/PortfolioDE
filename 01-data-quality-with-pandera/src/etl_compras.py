import pandas as pd
import pandera as pa
from modules.file_operation import le_arquivo_xlsx
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
