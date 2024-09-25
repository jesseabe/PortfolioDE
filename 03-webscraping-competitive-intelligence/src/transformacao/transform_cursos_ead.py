import pandas as pd
import sqlite3

class EADDataProcessor:
    def __init__(self, csv_path, db_path):
        self.csv_path = csv_path
        self.db_path = db_path
        self.df_ead = None

    def load_data(self):
        """Carrega os dados do arquivo CSV."""
        self.df_ead = pd.read_csv(self.csv_path)

    def clean_data(self):
        """Realiza o tratamento de dados no DataFrame."""
        self.df_ead['mensalidade_original'] = self.df_ead['mensalidade_original'].str.replace(',', '.')
        self.df_ead['mensalidade_original'] = pd.to_numeric(self.df_ead['mensalidade_original'], errors='coerce')
        
        self.df_ead['mensalidade_promo'] = (
            self.df_ead['mensalidade_promo']
            .str.replace('*', '', regex=False)  # Remove o asterisco
            .str.replace(',', '.')              # Substitui a vírgula por ponto
            .astype(float)                      # Converte para float
        )
        self.df_ead['mensalidade_promo'] = pd.to_numeric(self.df_ead['mensalidade_promo'], errors='coerce')

    def save_to_db(self):
        """Conecta ao banco de dados SQLite e salva os dados."""
        conn = sqlite3.connect(self.db_path)
        self.df_ead.to_sql('cursos_ead', conn, if_exists='replace', index=False)
        conn.close()

    def show_data(self, rows=5):
        """Exibe as primeiras linhas do DataFrame."""
        print(self.df_ead.head(rows))

# Exemplo de uso
if __name__ == "__main__":
    processor = EADDataProcessor('data/cursos_ead.csv', 'data/quotes.db')
    processor.load_data()
    processor.clean_data()
    processor.save_to_db()
    processor.show_data()
