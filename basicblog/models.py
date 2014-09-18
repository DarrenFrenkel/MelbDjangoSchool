from datetime import datetime, timedelta, time

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def recent_published(self):
        yesterday = datetime.now() - timedelta(days=1)
        return self.filter(created_at__gte=yesterday)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name="posts")

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("basicblog:blog-details", kwargs={"slug": self.slug})

class Comment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey(User, related_name="commenters")
    for_post =  models.ForeignKey(Post, related_name="comments")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.commenter.username + "-" + self.for_post.title
        super(Comment, self).save(*args,**kwargs)





