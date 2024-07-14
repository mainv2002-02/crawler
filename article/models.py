from django.db import models


class Article(models.Model):
    url = models.URLField('URL', max_length=255, unique=True)
    title = models.CharField('Title', max_length=255, blank=True)
    summary = models.TextField('Summary', blank=True, null=True)
    content = models.TextField('Content', blank=True, null=True)
    json = models.JSONField('Json', blank=True, null=True)
    data = models.JSONField('Data', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '-'.join([self.title, self.url])


class CrawlerConfig(models.Model):
    name = models.CharField('Name', max_length=255)
    url = models.URLField('URL', max_length=255, unique=True)
    title_pattern = models.TextField('Title Pattern', max_length=255)
    summary_pattern = models.TextField('Summary Pattern', blank=True, null=True)
    content_pattern = models.TextField('Content Pattern', blank=True, null=True)
    data = models.JSONField('Data', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
