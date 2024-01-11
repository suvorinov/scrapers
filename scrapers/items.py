# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime
from dataclasses import dataclass, field

import scrapy

now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


@dataclass
class Proxy:
    host: str = field(default='')
    port: int = field(default=80)
    anonymity: str = field(default='transparent')
    country: str = field(default='US')
    response_time: float = field(default=0.0)
    to_from: str = field(default='')
    last_checked: str = field(default=now)
