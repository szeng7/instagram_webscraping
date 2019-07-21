# Instagram Web Scraping

These are some spiders and script files that I made using Scrapy and Selenium.

### Scrapy Overview

The "hashtag.py" spider extracts the caption, image-url, number of likes, number of comments and owner name of a collection of posts under a specific hashtag that you give it. 

However, if you see the repo (instagram-caption-generator) for my other project, you'll see that this wasn't sufficient information for what I intended to use the dataset for, so I tried to obtain the number of followers of each of those users with another spider "user.py" so that I could normalize the data.

I was able to get the follower count of around 800 of the 50,000 users but ending up hitting a problem where only 90 of my requests were made at a time and when I tried to place a loop around how many times the spider was called, it seems like my spider was blocked. 

Reference for the hashtag spider: https://github.com/h4t0n/instagram-scraper

#### How To Use

When inside the outermost scrapy_instagram directory, call `scrapy crawl hashtag` or `scrapy crawl user` depending on which spider you want to use. 

For hashtag, you'll need to then enter the hashtag you want to scrape. 

For user, you'll need to then enter the name of the text file that contains all of the users you want to scrape the follower count from (one username per line). 

The output JSON file will be in `scrapy_instagram/scraped/`.

### Selenium Overview

Due to my scrapy spider being blocked, I switched to using Selenium. It is much simpler to understand but is also a lot slower. 

#### How To Use

Once again, you'll need to have a text file of all of the users you want to scrape the follower count from (I've simply hardcoded it as `user_followers.txt` but this can be easily changed).

Call `python extract.py` and it'll start reading from that file. It'll display a progress bar (mainly for the ETA estimate) and output to a file called `user_follower.pickle` which will contain a dictionary of key-user and value-follower_count pairs. 

Additionally, it'll write to that pickle file every 10 followers and when running, it will first try to load an existing `user_follower.pickle` before starting. The motivation behind this was because for the purposes in which I was using it, I had an extensive amount of accounts to go through (>50,000), which meant that running it in one sitting was impossible. This allowed for me to run it through multiple sessions by just looking at the most recent entry saved (which I have printed out to stdout) and then manually going through `user_followers.txt` and deleting everything up to that username. 

This process can be automatically done (just keep track of all of the usernames and then rewrite the new ones to the file) but at the volume I was working with, this would slow down my program drastically, so it was more worthwhile for me to manually delete the usernames after running it overnight. 