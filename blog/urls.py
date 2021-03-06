from django.conf.urls import patterns, include, url
from .views import PostListView, PostDetailView,CategoryPostListView, AboutPageView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^post/(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^category/(?P<slug>[-_\w]+)/$', CategoryPostListView.as_view(), name='category-list'),
    url(r'^about/$', AboutPageView.as_view(), name='about-page'),
)
