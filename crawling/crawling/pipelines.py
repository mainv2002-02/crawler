from article.models import Article
def clean_title(param):
    return param


def clean_critics_consensus(param):
    return " ".join(param)


def clean_average_grade(param):
    param = param.strip().replace("/5", "")
    return param


def clean_poster(param):
    if param:
        param = param[0]["path"]
    return param


def clean_amount_reviews(param):
    return param.strip()


def clean_approval_percentage(param):
    return param.strip().replace("%", "")


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        summary = item['summary']
        content = item['content']

        Article.objects.create(
            url='https://baike.baidu.com/',
            title=title,
            summary=summary,
            # content='content'
        )
        return item
