from faker import Faker
import pandas as pd
import random

# Inicializando Faker
faker = Faker('pt_BR')

# Definindo algumas categorias e produtos para simular
categorias = ['Eletrônicos', 'Móveis', 'Roupas', 'Brinquedos', 'Alimentos']
produtos = {
    'Eletrônicos': ['Smartphone', 'Laptop', 'Tablet'],
    'Móveis': ['Mesa', 'Cadeira', 'Sofá'],
    'Roupas': ['Camiseta', 'Calça', 'Jaqueta'],
    'Brinquedos': ['Carrinho', 'Boneca', 'Jogo de tabuleiro'],
    'Alimentos': ['Arroz', 'Feijão', 'Macarrão']
}

# Função para gerar dados de DRE
def gerar_dados_dre(num_linhas=200):
    dados = []
    for _ in range(num_linhas):
        categoria = random.choice(categorias)
        produto = random.choice(produtos[categoria])
        
        receita_bruta = round(random.uniform(1000, 50000), 2)
        impostos = round(receita_bruta * random.uniform(0.05, 0.2), 2)
        receita_liquida = receita_bruta - impostos
        
        cmv = round(receita_liquida * random.uniform(0.3, 0.7), 2)
        lucro_bruto = receita_liquida - cmv
        
        despesa_operacional = round(lucro_bruto * random.uniform(0.1, 0.4), 2)
        lucro_liquido = lucro_bruto - despesa_operacional
        
        linha = {
            'Data': faker.date_this_year(),
            'Categoria': categoria,
            'Produto': produto,
            'Receita Bruta': receita_bruta,
            'Impostos': impostos,
            'Receita Líquida': receita_liquida,
            'CMV': cmv,
            'Lucro Bruto': lucro_bruto,
            'Despesa Operacional': despesa_operacional,
            'Lucro Líquido': lucro_liquido
        }
        dados.append(linha)
    
    return pd.DataFrame(dados)


if __name__ == "__main__":
    # Gerar a base de dados
    df_dre = gerar_dados_dre(1000000)
    df_dre.to_csv("data/dre.csv")
    print(df_dre.head())
    
    df_dre2 = gerar_dados_dre(1000000)
    df_dre2.to_csv("data/dre2.csv")
    print(df_dre2.head())
    
    df_dre3 = gerar_dados_dre(1000000)
    df_dre3.to_csv("data/dre3.csv")
    print(df_dre3.head())

    df_dre4 = gerar_dados_dre(1000000)
    df_dre4.to_csv("data/dre4.csv")
    print(df_dre4.head())

    df_dre5 = gerar_dados_dre(1000000)
    df_dre5.to_csv("data/dre5.csv")
    print(df_dre5.head())

