import pandas as pd

def renomeia_colunas(df: pd.DataFrame, renomeia_colunas: dict) -> pd.DataFrame:
    df.rename(columns=renomeia_colunas, inplace=True)
    return df