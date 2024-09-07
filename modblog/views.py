from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Queryset selects posts to display.
    Status=1 selects only published posts
    Post grabs available object or returns 404 error if there is none
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request, "blog/post_detail.html", {"post": post},
    )
