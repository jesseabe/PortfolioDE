import pandas as pd

def le_arquivo_xlsx(dir_arquivo: str, renomeia_colunas: dict) -> pd.DataFrame:
    df = pd.read_excel(dir_arquivo)
    df.rename(columns=renomeia_colunas, inplace=True)
    return df

def transforma_dados_generico(df: pd.DataFrame, drop_subset: list) -> pd.DataFrame:
    df_transformado = df.copy()
    df_transformado = df_transformado.dropna(subset=drop_subset)
    df_transformado = df_transformado.drop_duplicates(subset=drop_subset)
    return df_transformado