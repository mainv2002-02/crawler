from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.spiders import Spider


class Web(Spider):
    name = ''
    allowed_domains = []
    start_urls = []
    pattern = ''
    base_url = ''

    def parse(self, response: Response, **kwargs: Any) -> Any:
        yield self.parse_content(response)

        # rows = response.xpath(self.pattern).extract()
        #
        # for row in rows:
        #     link = self.base_url + row
        #     yield scrapy.Request(url=link, callback=self.parse_item)

    def parse_item(self, response: Response):
        pass

    def parse_content(self, response: Response):
        pass
