from crawling.items import ArticleItem
from crawling.spiders.web import Web
from scrapy.selector import Selector
from w3lib import html
from scrapy.http import Request, Response
from article.models import Article


class Baidu(Web):
    name = 'baidu'
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E7%9F%B3%E6%98%8A/9138725'
    ]
    patterns = {
        'title': '//h1[@class="lemmaTitle_kEoDP J-lemma-title"]/text()',
        'summary': '//div[@class="lemmaSummary_oJtZ8 J-summary"]/div//text()',
        'content': '//div[@class="J-lemma-content"]/div',
    }

    content_pattern = '//div[@class="contentTab__I5si curTab_NVLbk"]/div'

    def start_requests(self):
        print('===')
        rows = Article.objects.filter(summary='').order_by('id')[:5]
        for row in rows:
            yield Request(row.url, dont_filter=True)
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
            if 'paraTitle_X1rxd level-1_smEgo' in item:
                dict = {}
                contents.append(dict)
                dict['h2'] = Selector(text=item).xpath("//text()").extract_first()
                dict['h3'] = []
                h3 = {
                    'text': '',
                    'content': []
                }
                dict['h3'].append(h3)
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

        article = ArticleItem(title=title, url=response.request.url, summary=summary, content=contents)
        article.save()
        return article
