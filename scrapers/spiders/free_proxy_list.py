# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-12-21 09:30:05
# @Last Modified by:   suvorinov
# @Last Modified time: 2024-01-05 20:21:48

import pathlib

from scrapy.spiders import Spider
from scrapy.http import Request

from py_random_useragent import UserAgent
from scrapers.settings import FREE_PROXY_DATA_PATH
from scrapers.models.proxy import Proxy


DATA_PATH = pathlib.Path.home() / 'free_proxy'


class FreeProxyListSpider(Spider):
    name = "free_proxy_list"

    allowed_domains = ["free-proxy-list.net"]
    start_urls = ["https://free-proxy-list.net/"]

    file_json = FREE_PROXY_DATA_PATH / f"{name}.json"
    file_csv = FREE_PROXY_DATA_PATH / f"{name}.csv"

    """
    'ftp://suvorinov:669498surik@dev.dev/%(name_ru)s/%(country)s/%(city)s.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
        'overwrite': True
    },
    'ftp://suvorinov:669498surik@dev.dev/%(name_ru)s/%(country)s/%(city)s.json': { # noqa
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
        'overwrite': True
    },
    'ftp://suvorinov:669498surik@dev.dev/%(name)s/%(city)s.csv': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
        'overwrite': True
    },
    """

    custom_settings = {
        'FEEDS': {
            pathlib.Path(file_json): {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
                'overwrite': True
            },
            pathlib.Path(file_csv): {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True
            },
        }}

    def __init__(self, *args, **kwargs):
        super(FreeProxyListSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            headers = {
                'User-Agent': UserAgent().get_ua()
            }
            yield Request(
                url=url,
                headers=headers
            )

    def parse(self, response):

        try:
            for tr in response.xpath('//tbody/tr'):
                tds = tr.xpath('.//td')
                # print(tds)
                if tds:
                    item = Proxy()
                    item.host = tds[0].xpath('text()').get(None)
                    item.port = tds[1].xpath('text()').get(None)
                    item.to_from = self.start_urls[0]
                # item['desc'] = tds[1].xpath('text()').getall()[1:]
                    yield item
        except Exception:
            self.logger.error('Exception during success_parse', exc_info=True)
