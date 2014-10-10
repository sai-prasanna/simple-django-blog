from django.conf.urls import patterns, include, url
from .views import PostListView, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post-detail'),
)
