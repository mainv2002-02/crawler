# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from article.models import Article
#from scrapy_djangoitem import DjangoItem
#from article.models import Article


class ArticleItem(DjangoItem):
    django_model = Article
    title = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
