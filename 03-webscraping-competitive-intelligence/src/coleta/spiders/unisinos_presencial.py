import scrapy

class UnisinosPresencialSpider(scrapy.Spider):
    name = "unisinos_presencial"
    allowed_domains = ["unisinos.br"]
    start_urls = ["https://www.unisinos.br/graduacao/cursos?modalidade=P"]

    #fetch('https://www.unisinos.br/graduacao/cursos?modalidade=P')

    def parse(self, response):
        # Obtém todos os links dos cursos
        cursos = response.css('a.text-white::attr(href)').getall()
        
        # Itera sobre cada curso
        for curso in cursos:
            curso_url = response.urljoin(curso)  # Constrói a URL completa
            # Faz uma requisição para cada página de curso
            yield scrapy.Request(curso_url, callback=self.parse_curso)

    def parse_curso(self, response):
        # Extrai as informações desejadas de cada página do curso
        tipo_curso = response.css('div.sppb-addon-text::text').getall()[0].strip()
        curso = response.css('h1::text').get().strip()
        turno = response.css('div.sppb-addon-text::text').getall()[1].strip()
        duracao_curso = response.css('div.sppb-addon-text::text').getall()[2].strip()

        # Retorna as informações coletadas  
        yield {
            'tipo_curso': tipo_curso,
            'curso': curso,
            'turno': turno,
            'duracao': duracao_curso
        }
