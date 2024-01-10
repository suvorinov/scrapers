# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem


class ScrapersPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatesProxyPipeline:

    def __init__(self, *args, **kwargs):
        super(DuplicatesProxyPipeline, self).__init__(*args, **kwargs)

        self.hash_proxy = {}

    def process_item(self, item, spider):
        host = item.host
        port = item.port

        _hash = '%s:%s' % (host, port)
        if _hash in self.hash_proxy:
            raise DropItem(f"Duplicate item found: {_hash!r}")
        self.hash_proxy[_hash] = True
        return item
