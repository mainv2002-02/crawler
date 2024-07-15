from article.models import Article


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        # Article.objects.update_or_create(url=item.url,
        #                                  defaults={'title': item.title, 'summary': item.summary,
        #                                            'content': item.content},
        #                                  create_defaults={'url': item.url, 'title': item.title,
        #                                  'summary': item.summary, 'content': item.content})
        try:
            item = Article.objects.get(url=item.url)
            print('=====')
            print(item)
        except Article.DoesNotExist:
            print('------')
            Article.objects.create(title=item.title, url=item.url, summary=item.summary, content=item.content)
        else:
            print('......')
            item = Article.objects.filter(url=item.url).update(title=item.title, summary=item.summary,
                                                               content=item.content)
        return item
