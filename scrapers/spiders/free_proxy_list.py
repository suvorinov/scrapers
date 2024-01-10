# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-12-21 09:30:05
# @Last Modified by:   Suvorinov Oleg
# @Last Modified time: 2024-01-10 12:12:51

import pathlib
from multiprocessing.dummy import Pool

from scrapy.spiders import Spider
from scrapy.http import Request

from scrapers.settings import FREE_PROXY_DATA_PATH
from scrapers.models.proxy import Proxy

from py_random_useragent import UserAgent


USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"


class FreeProxyListSpider(Spider):
    name = "free_proxy_list"

    allowed_domains = ["free-proxy-list.net"]
    # start_urls = ["https://free-proxy-list.net/"]
    "https://scrape-it.cloud/free-proxy-list"

    file_json = FREE_PROXY_DATA_PATH / f"{name}.json"

    custom_settings = {
        'FEEDS': {
            pathlib.Path(file_json): {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
                'overwrite': True
            },
        }}

    def start_requests(self):
        headers = {
            'User-Agent': USER_AGENT  # UserAgent().get_ua()
        }
        yield Request(
            url="https://free-proxy-list.net/",
            callback=self.parse,
            headers=headers,
            meta={
                "to_from": "https://free-proxy-list.net/"
            }
        )

        yield Request(
            url="https://scrape-it.cloud/free-proxy-list",
            callback=self.parse,
            headers=headers,
            meta={
                "to_from": "https://scrape-it.cloud"
            }
        )

    def parse(self, response):

        try:
            for tr in response.xpath('//tbody/tr'):
                tds = tr.xpath('.//td')
                if tds:
                    item = Proxy()
                    item.host = tds[0].xpath('text()').get(None)
                    item.port = tds[1].xpath('text()').get(None)
                    item.to_from = response.meta['to_from']
                    yield item
        except Exception:
            self.logger.error('Exception during parse proxy list', exc_info=True) # noqa
