from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

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
    Comments are retrieved and then displayed based on when they were posted
    Only approved comments are retrieved
    A Form is provided for users to submit comments
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    comment_form = CommentForm()

    return render(
        request, "modblog/post_detail.html",
        context={
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,} 
    )

