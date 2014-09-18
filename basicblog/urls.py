from django.conf.urls import patterns, include, url

urlpatterns = patterns('basicblog.views',
    url(r'^$', 'blog_posts', name='blog-posts' ),
    url(r'^(?P<slug>[-\w]+)/$', 'blog_details', name='blog-details' ),
)