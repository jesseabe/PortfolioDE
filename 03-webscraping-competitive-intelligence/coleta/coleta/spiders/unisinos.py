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
            yield {
                'course': curso  # Aqui usamos 'curso' diretamente
            }

