from article.models import Article


class CrawlingPipeline(object):
    def process_item(self, item, spider):
            # title = item['title']
            # summary = item['summary']
            # content = item['content']

            # Article.objects.create(
            #     url='https://baike.baidu.com/',
            #     title=title,
            #     summary=summary,
            #     # content='content'
            # )
        item.save()
        return item
