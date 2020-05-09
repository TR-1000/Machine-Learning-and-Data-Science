import scrapy


class ResultsSpider(scrapy.Spider):
    name = "results"
    start_urls = [
        'https://www.amazon.com/s?k=elder scrolls&ref=nb_sb_noss_1',
    ]

    def parse(self, response):
        for item in response.css('.s-result-item'):
            yield {
                'title': item.css("h2 span::text").get()
            }
