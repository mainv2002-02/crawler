from django.contrib import admin

# # Register your models here.
from .models import Article
# from .models import CrawlerConfig
#
#
# class ArticleAmin(Article):
#     pass
#
#
# class CrawlerConfigAdmin(CrawlerConfig):
#     pass
#

admin.site.register(Article)
