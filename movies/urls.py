from django.conf.urls.defaults import *

from movies import views

urlpatterns = patterns('',
    # ex: /movies/
    url(r'^$', views.index, name='index'),
    # ex: /movies/5/
    url(r'^(?P<pk>[a-z\d]+)/$', views.detail, name='detail'),
    # url(r'^post/(?P<pk>[a-z\d]+)/$', post_detail, name='post_detail'),
    # url(r'^$', post_list, name='post_list'),
    # ex: /movies/5/results/
    url(r'^(?P<movie_id>\d+)/results/$', views.results, name='results'),
    # ex: /movies/5/vote/
    url(r'^(?P<movie_id>\d+)/vote/$', views.vote, name='vote'),
)