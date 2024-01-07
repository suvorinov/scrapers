# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2024-01-05 09:35:06
# @Last Modified by:   suvorinov
# @Last Modified time: 2024-01-05 09:39:43

from scrapy.crawler import CrawlerProcess

from spiders.free_proxy_list import FreeProxyListSpider


process = CrawlerProcess()


def main():
    process.crawl(FreeProxyListSpider)
    process.start()


if __name__ == '__main__':
    main()
