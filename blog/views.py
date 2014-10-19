from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category


class PostListView(generic.ListView):


    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10


class PostDetailView(generic.DetailView):


    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class CategoryPostListView(generic.ListView):


    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.queryset = Post.objects.filter(categories__slug=self.slug)
        return super(CategoryPostListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.slug)
        return context


class AboutPageView(generic.TemplateView):


    template_name = "blog/about.html"

