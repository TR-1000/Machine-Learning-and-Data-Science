import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('a.tag::text').getall(),
            }

        # recursively follow the link to the next page, extracting data from it:

        # next_page =  response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        #
        # for href in response.css('li.next a::attr(href)'):
        #     yield respose.follow(href, callback=self.parse)

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
