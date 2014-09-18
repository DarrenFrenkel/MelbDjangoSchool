import pudb
import datetime

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils import timezone


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    num_of_articles = models.IntegerField(blank=True, null=True, default=0)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    reporter = models.ForeignKey(Reporter, related_name='articles')
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('headline',)

    def __unicode__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)
        instance = self.reporter
        instance.num_of_articles = self.reporter.articles.count()
        instance.save()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@receiver(post_delete, sender=Article)
def update_article_num(sender, **kwargs):
    reporter_instance = kwargs.get('instance').reporter
    reporter_instance.num_of_articles = reporter_instance.articles.count()
    reporter_instance.save()