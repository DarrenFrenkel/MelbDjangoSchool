from django.db import models
from django.db.models.signals import pre_delete

from .models import Article

@receiver(pre_delete, sender=Article)
def update_article_num(self, sender, **kwargs):
    instance = sender.reporter
    current_article_num = sender.reporter.article_set.count()
    instance.num_of_articles = current_article_num - 1
    instance.save()
