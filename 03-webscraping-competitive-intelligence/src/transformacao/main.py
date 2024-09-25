from transformacao.transform_cursos_ead import EADDataProcessor
from transformacao.transform_cursos_presencial import PresencialDataProcessor

def main():
    # Processar os dados EAD
    processor_ead = EADDataProcessor('data/cursos_ead.csv', 'data/quotes.db')
    processor_ead.load_data()
    processor_ead.clean_data()
    processor_ead.save_to_db()
    processor_ead.show_data()

    # Processar os dados Presencial
    processor_presencial = PresencialDataProcessor('data/cursos_presencial.csv', 'data/quotes.db')
    processor_presencial.load_data()
    processor_presencial.clean_data()
    processor_presencial.save_to_csv()
    processor_presencial.save_to_db()
    processor_presencial.show_data()

if __name__ == "__main__":
    main()

