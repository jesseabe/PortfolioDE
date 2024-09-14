import streamlit as st
import pandas as pd
from pydantic import ValidationError
from contratos.schema import ProdutoSchema
from file_operation import renomeia_colunas  
import os

# Funções da UI
def upload_file_ui():
    return st.file_uploader("Escolha o arquivo Excel", type="xlsx")

def display_errors(errors):
    for error in errors:
        st.error(error)

def confirm_upload():
    return st.button("Subir Dados")

# Função para processar o arquivo Excel
def process_excel(file):
    renomeia_colunas_dict = {
        'Nº doc.': 'NumDoc',
        'Cen.': 'Centro',
        'Referência': 'Referencia',
        'Doc.compra': 'Doc_Compra',
        'Dt.lçto.': 'Data_Lancamento',
        'Dt.entr.': 'Data_Entrada',
        'EmissFatur': 'EmissFatur',
        'Nome 1': 'Fornecedor',
        'Data base': 'Data_Base',
        'Dia1': 'Dia',
        'Material': 'ID_Material',
        'Texto breve de material': 'Desc_Material',
        'Quantidade': 'Quantidade',
        'UMP': 'UMB',
        'UMP.1': 'UMB_Desc',
        'Montante': 'Montante',
        'Moeda': 'Moeda',
        'CPgt': 'CPgt',
        'Grupo': 'Grupo',
        'Denominação': 'Denominacao',
        'ClAv.': 'ClAv',
        'Taxa câmbio': 'Taxa_Cambio',
        'Cta.recon.': 'Conta_reconsiliacao',
        'Dt.remessa': 'Data_remessa'
    }
    try:
        df = pd.read_excel(file)
        df = renomeia_colunas(df, renomeia_colunas_dict)
        
        # Forçar conversão de tipos antes de validar
        df = df.copy()
        df = df.dropna(subset=['ID_Material'])
        df = df.drop_duplicates(subset=['NumDoc', 'Centro', 'Referencia', 'Doc_Compra', 'Data_Lancamento', 'Data_Entrada', 'EmissFatur', 'Fornecedor', 'Data_Base', 'Dia', 'ID_Material', 'Quantidade', 'UMB', 'UMB_Desc', 'Montante', 'Moeda', 'CPgt', 'Grupo', 'Denominacao', 'ClAv', 'Taxa_Cambio', 'Conta_reconsiliacao', 'Data_remessa'])  
        df = df.fillna("n/a")
        colunas_para_conversao = ['NumDoc', 'Doc_Compra', 'EmissFatur', 'Dia', 'ID_Material', 'ClAv', 'Conta_reconsiliacao']
        
        def converte_para_string(x):
            if isinstance(x, float):
                if x.is_integer():
                    return str(int(x))
                else:
                    return str(x)
            elif pd.isna(x):
                return "n/a"
            return str(x)
        
        df[colunas_para_conversao] = df[colunas_para_conversao].applymap(converte_para_string)
        
        df['Taxa_Cambio'] = df['Taxa_Cambio'].str.replace(',', '.').astype(float)
        
        errors = validate_dataframe(df)
        return df, errors
    except Exception as e:
        # Tratamento de erro
        column_names = df.columns.tolist() if 'df' in locals() else 'N/A'
        error_message = f"Erro na leitura do arquivo: {str(e)}"
        if column_names != 'N/A':
            error_message += f"\nColunas do DataFrame: {', '.join(column_names)}"
            for column in column_names:
                try:
                    sample_data = df[column].head().tolist()  # Obtém amostras dos dados da coluna
                except KeyError:
                    sample_data = 'Coluna não encontrada'
                error_message += f"\nDados da coluna '{column}': {sample_data}"
        return None, [error_message]


# Função para validar o DataFrame usando ProdutoSchema
def validate_dataframe(df):
    errors = []
    required_columns = ProdutoSchema.__annotations__.keys()
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        errors.append(f"Faltam colunas no arquivo: {', '.join(missing_columns)}")
    
    for _, row in df.iterrows():
        try:
            ProdutoSchema(**row.to_dict())
        except ValidationError as e:
            errors.append(f"Erro de validação na linha {row.name + 1}: {e}")
    
    return errors

# Função principal
def main():
    st.title("Upload de Arquivos xlsx com validador")

    uploaded_file = upload_file_ui()
    if uploaded_file is not None:
        # Salvar o arquivo no disco
        file_path = os.path.join("uploaded_files", uploaded_file.name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Processar o arquivo
        data, errors = process_excel(file_path)
        if errors:
            display_errors(errors)
        else:
            if confirm_upload():
                st.success("Dados enviados com sucesso!")
                # Opcional: mostrar uma amostra dos dados
                st.dataframe(data)

if __name__ == "__main__":
    main()
