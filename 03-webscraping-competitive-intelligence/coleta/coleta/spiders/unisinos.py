import scrapy


class UnisinosSpider(scrapy.Spider):
    name = "unisinos"
    allowed_domains = ["ead.unisinos.br"]
    start_urls = ["https://ead.unisinos.br/cursos-graduacao"]

    def parse(self, response):
        pass
