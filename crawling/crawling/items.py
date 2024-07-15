from scrapy_djangoitem import DjangoItem

from article.models import Article


class ArticleItem(DjangoItem):
    django_model = Article
