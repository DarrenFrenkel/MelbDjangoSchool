from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'melbdjangoschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^testhttp/', include('testhttp.urls', namespace='testhttp')),
)
