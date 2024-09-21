import pandas as pd

df = pd.read_csv('data/cursos_ead.csv')

#Realizando o tratameto nos valores 
df['mensalidade_original'] = df['mensalidade_original'].str.replace(',', '.')
df['mensalidade_original'] = pd.to_numeric(df['mensalidade_original'], errors='coerce')
df['mensalidade_promo'] = (
    df['mensalidade_promo']
    .str.replace('*', '', regex=False)  # Remove o asterisco
    .str.replace(',', '.')              # Substitui a vírgula por ponto
    .astype(float)                      # Converte para float
)
df['mensalidade_promo'] = pd.to_numeric(df['mensalidade_promo'], errors='coerce')

#Salvando os dados transformados
df.to_csv('data/cursos_ead_transformado.csv', index=False)

