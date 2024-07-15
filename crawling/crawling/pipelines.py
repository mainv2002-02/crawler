from article.models import Article


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        Article.objects.update_or_create(
            title=item.title, url=item.url, summary=item.summary, content=item.content,
            defaults={'url': item.url})
        return item
