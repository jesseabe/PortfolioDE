import scrapy

class UnisinosSpider(scrapy.Spider):
    name = "unisinos"
    allowed_domains = ["ead.unisinos.br"]
    start_urls = ["https://ead.unisinos.br/cursos-graduacao"]

    def parse(self, response):
        # Obtém todos os links dos cursos
        cursos = response.css('a.course-link-card::attr(href)').getall()
        
        # Itera sobre cada curso
        for curso in cursos:
            curso_url = response.urljoin(curso)  # Constrói a URL completa
            # Faz uma requisição para cada página de curso
            yield scrapy.Request(curso_url, callback=self.parse_curso)

    def parse_curso(self, response):
        # Extrai as informações desejadas de cada página do curso
        tipo_curso = response.css('span.subtitle[data-gtm-course-category="true"]::text').get()
        curso = response.css('h1[data-gtm-course-name="true"]::text').get()
        mensalidade_original = response.css('p.mensalidade.original[data-gtm-course-price]::text').get()
        mensalidade_promo = response.css('p.mensalidade.promo[data-gtm-course-price]::text').get()
        duracao = response.css('span svg + span::text').get()  # Ajuste conforme o layout do site

        # Retorna as informações coletadas
        yield {
            'tipo_curso': tipo_curso,
            'curso': curso,
            'mensalidade_original': mensalidade_original,
            'mensalidade_promo': mensalidade_promo,
            'duracao': duracao
        }


