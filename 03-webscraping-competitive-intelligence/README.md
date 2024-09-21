# Projeto de Web Scraping para Inteligencia Competitiva

1. Abre o shell do scrapy
```bash
scrapy shell
```

2. Acessa o site para realizar o crawling
```bash
fetch('https://ead.unisinos.br/cursos-graduacao/administracao')
```

3. Pega o response do site (verifica se o site aceita a requisição)
```bash
response
```

4. Retorna todo o texto da página
```bash
response.text
```

5. Para rodar o webscraping no git bash: 
```bash
scrapy crawl unisinos -o ../data/cursos_ead.csv
```

6. Para rodar a ETL
```bash
python src/transformacao/main.py
```