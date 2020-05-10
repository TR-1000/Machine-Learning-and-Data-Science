import scrapy
from scrapy.loader import ItemLoader
from wikiSpider.items import WikispiderItem

class ArticleSpider(scrapy.Spider):
    name = 'articles'
    start_urls = [
        'http://en.wikipedia.org/wiki/Python_'
        '%28programming_language%29',
        'https://en.wikipedia.org/wiki/Functional_programming',
        'https://en.wikipedia.org/wiki/Monty_Python'
    ]

    # # scrape to dict
    # def parse(self, response):
    #     url = response.url
    #     title = response.css('h1::text').extract_first()
    #     print(f'URL is: {url}')
    #     print(f'Title is {title}')
    #
    #     yield {
    #         'url':url,
    #         'title': title,
    #     }


    # scrape to scrapy item
    def parse(self, response):
        article = ItemLoader(item=WikispiderItem(),response=response)
        article.add_value('url', response.url)
        article.add_css('title', ("h1::text"))
        return article.load_item()



# run spider > scrapy crawl articles
# export feeds > scrapy crawl articles -o articles.json
# inspect page in shell > scrapy shell 'https://en.wikipedia.org/wiki/Python_(programming_language)'
