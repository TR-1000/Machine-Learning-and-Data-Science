# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# similar to models.py in Django
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field
import pprint
pp = pprint.PrettyPrinter(indent=4)

class LivingSocialDeal(Item):
    # Livingsocial container (dictionary-like object) for scraped data.
    # LivingSocialDeal class, will inherit from Item.

    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()

    # In scrapy, there are no other field types, unlike Django. So, use Field().




deal = LivingSocialDeal(title="$20 off all PC Games", price="20")

pp.pprint(deal)
