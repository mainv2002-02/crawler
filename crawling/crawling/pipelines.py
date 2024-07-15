from article.models import Article


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        Article.objects.filter(url=item.url).update(
            title=item.title, url=item.url, summary=item.summary, content=item.content)
        return item
