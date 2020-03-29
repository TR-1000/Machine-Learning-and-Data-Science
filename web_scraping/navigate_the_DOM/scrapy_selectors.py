from scrapy.selector import Selector
import requests

response = requests.get("https://stackoverflow.com/questions")
selector = Selector(response)

divs = selector.xpath('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/text()')
[x.extract() for x in divs]

summaries = selector.xpath('//div[@class="summary"]/h3')
[x.extract() for x in summaries.xpath('a[@class="question-hyperlink"]/text()')]
