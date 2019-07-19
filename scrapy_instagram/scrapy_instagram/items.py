# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Post(Item):
    # define the fields for your item here like:
    id = Field()
    shortcode = Field()
    caption = Field()
    display_url = Field()
    likes = Field()
    comments = Field()
    owner_name = Field()
    taken_at_timestamp = Field()
    pass

class User(Item):
    user = Field()
    followers = Field()
    pass
