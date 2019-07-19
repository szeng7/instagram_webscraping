# Instagram Webscraping

These are some spiders and script files that I made using Scrapy.

The "hashtag" spider extracts the caption, image-url, number of likes, number of comments and owner name of a collection of posts under a specific hashtag that you give it. 

However, if you see the repo (instagram-caption-generator) for my other project, you'll see that this wasn't sufficient information, so I tried to obtain the number of followers of each of those users with another spider "user."

I was able to get the follower count of around 800 of the 50,000 users but ending up hitting a problem where only 90 of my requests were made at a time and when I tried to place a loop around how many times the spider was called, it seems like my spider was blocked. 

I will be attempting to use Selenium and put that spider here if that works.

Reference for the hashtag spider: https://github.com/h4t0n/instagram-scraper