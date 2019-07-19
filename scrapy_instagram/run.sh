#! /usr/bin/env bash

scrapy crawl user
python update_users.py

printf "DONE WITH A CYCLE\n\n\n\n\n\n\n\n\n"
