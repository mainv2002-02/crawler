from crawling.spiders.web import Web
from scrapy.http import Response
from scrapy.selector import Selector
from w3lib import html


class Pixiv(Web):
    name = 'pixiv'
    allowed_domains = ['dic.pixiv.net']
    start_urls = [
        'https://dic.pixiv.net/a/%E3%82%BC%E3%83%BC%E3%83%AA%E3%82%A8'
    ]
    patterns = {
        'title': '//h1[@id="article-name"]/text()',
        'summary': '//div[@data-header-id="h2_0"]/p//text()',
        'content': '//div[@class="sc-d805894c-0 ezvwjv"]/div',
    }

    content_pattern = '//div[@class="contentTab__I5si curTab_NVLbk"]/div'

    # def parse(self, response: Response, **kwargs: Any) -> Any:
    #     contents = Selector(response).xpath(self.pattern)
    #
    #     for item in contents:
    #         yield self.parse_content(item)
    #
    #     print("END -------\n\r")

    def parse_content(self, response: Response):
        title = Selector(response).xpath(self.patterns['title']).extract_first()
        summary = Selector(response).xpath(self.patterns['summary']).extract()
        contents = []
        dict = {}
        h3 = {}
        for item in Selector(response).xpath(self.patterns['content']).extract():
            if '<h2 class="' in item:
                dict = {}
                contents.append(dict)
                dict['h2'] = Selector(text=item).xpath("//text()").extract_first()
                dict['h3'] = []
                h3 = {
                    'text': '',
                    'content': []
                }
                dict['h2'].append(h3)
                dict['content'] = []
            elif 'paraTitle_X1rxd level-2_gaY8k' in item:
                h3["text"] = Selector(text=item).xpath("//text()").extract_first()
            elif 'para_OEbze content_roDnL MARK_MODULE' in item:
                h3['content'].append(' .'.join(Selector(text=item).xpath("//text()").extract()))
            elif 'data-module-type="table"' in item:
                content = Selector(text=item).xpath("//table").extract_first()
                h3['content'].append(html.remove_tags(text=content, keep=['table', 'tr', 'th', 'tbody', 'td']))
            else:

                pass
        print("--------\n")
