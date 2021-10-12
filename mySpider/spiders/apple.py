import scrapy
from bs4 import BeautifulSoup
class AppleSpider(scrapy.Spider):
    name = "apple"

    def start_requests(self):
        urls = ['https://developers.messagebird.com/api/conversations/#api-endpoint',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page=response.url.split("/")[-1]
        filename=f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
