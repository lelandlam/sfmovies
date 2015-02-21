from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfmovies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movies.views.movie', name='home'),
    url(r'^bootstrap', 'movies.views.bootstrap', name='bootstrap'),
    url(r'^contact', 'movies.views.contact', name='contact'),
    url(r'^add', 'movies.views.add', name='add'),
    url(r'^test', 'movies.views.test', name='test'),
)
