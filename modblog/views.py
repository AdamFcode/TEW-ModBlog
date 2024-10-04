from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    # Queryset populates page with all published(status 1) posts
    # Template name dictates which template to load and render
    # Paginate by decides the number of posts per page
    queryset = Post.objects.filter(status=1)
    template_name = "modblog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    # Queryset selects posts to display.
    # Status=1 selects only published posts.
    # Post grabs available object or returns.
    # 404 error if there is none.
    # Comments are retrieved and then displayed
    # based on when they were posted.
    # Only approved comments are retrieved.
    # A Form is provided for users to submit comments.
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment succeessfully added. Pending approval.'
            )
    comment_form = CommentForm()

    return render(
        request, "modblog/post_detail.html",
        context={
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form, }
    )


def comment_edit(request, slug, comment_id):
    # Allows the editing of comments
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Update successful.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error. Please try again.')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    # Allows the deletion of comments
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Error. Please try again')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# View for Custom Error 404
def error_404(request, exception):
    return render(request, 'modblog/templates/404.html', status=404)
