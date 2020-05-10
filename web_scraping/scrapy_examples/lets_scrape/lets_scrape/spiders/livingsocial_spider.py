import scrapy
# from scrapy.crawler import CrawlerProcess
# need to disable some setting in settings.py

class LivingsocialSpider(scrapy.Spider):
    name = 'living_social'
    # Spider for regularly updated livingsocial.com site, San Antonio Page

    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/browse/san-antonio"]

    def parse(self, response):
        for result in response.xpath('//div[@id="pull-results"]//div[@class="cui-content "]'):

            subtitle = result.css('.cui-udc-subtitle::text').get()
            if subtitle != None:
                subtitle = subtitle.strip()
            else:
                subtitle = ""

            location = result.css('span.cui-location-name::text').get()
            if location != None:
                location = location.strip()
            else:
                location = ""


            yield {
                'link': result.xpath('.//a/@href').get(),
                'image': result.xpath('.//img')[1].xpath('.//@data-srcset').get().strip().split(" ")[0],
                'title': result.css('.cui-udc-title::text').get().strip(),
                'subtitle': subtitle,
                'location': location,
                'price': result.css('div.cui-price-discount::text').get(),
                'original_price': result.css('.cui-price-original::text').get(),
                }