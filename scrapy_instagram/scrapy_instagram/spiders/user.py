# -*- coding: utf-8 -*-
import scrapy
import json
import time
import os.path

from scrapy.exceptions import CloseSpider

from scrapy_instagram.items import User

class InstagramSpider(scrapy.Spider):
    name = "user"  # Name of the Spider, required value
    custom_settings = {
        'FEED_URI': './scraped/%(name)s/%(date)s',
    }
    checkpoint_path = './scraped/%(name)s/.checkpoint'

    def __init__(self, file=''):
        self.file = file
        self.has_next = True
        if file == '':
            self.file = input("Name of the file of usernames? ")
        self.counter = 0
        with open(self.file, 'r') as f:
            self.users = f.readlines()
        self.user = self.users[0].strip('\n')
        self.start_urls = ["https://www.instagram.com/"+self.user+"/?__a=1"]
        self.date = time.strftime("%d-%m-%Y_%H")
        self.checkpoint_path = './scraped/%s/.checkpoint' % ("users")
        self.readCheckpoint()

    def readCheckpoint(self):
        filename = self.checkpoint_path
        if not os.path.exists(filename):
            self.last_crawled = ''
            return
        self.last_crawled = open(filename).readline().rstrip()

    # Entry point for the spider
    def parse(self, response):

        for user in self.users:
            user = user.strip('\n')
            yield scrapy.Request("https://www.instagram.com/"+user+"/?__a=1", callback=self.parse_post)

    def parse_post(self, response):
        graphql = json.loads(response.text)
        media = graphql['graphql']['user']
        yield self.makeUser(media)

    def makeUser(self, media):
        followers='0'
        try:
            followers=media['edge_followed_by']['count']
        except:
            followers='0'
        print(f"{media['username']}, {followers}")
        return User(user=media['username'],
                    followers=followers)
