from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    """
    Queryset populates page with all published(status 1) posts
    Template name dictates which template to load and render
    Paginate by decides the number of posts per page
    """
    queryset = Post.objects.filter(status=1)
    template_name = "modblog/index.html"
    paginate_by = 4
