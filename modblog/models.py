from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    The Post Model allows users to submit a post to the blog
    It requires a title, a unique slug and the name of the mod-maker if applicable
    The users name is displayed as is the date and time the post was created
    Content provides a textfield for the main body of the post
    A status setting referances the above constant and defines publication status
    The excerpt allows users to view a short excerpt of the content without clicking the post
    Any edits to the post are timestamped by updated_on 
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    mod_maker = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    """
    The Meta class orders the blog posts on the page
    """
    class Meta:
        ordering = ["-created_on"]

    """
    The __str__ method allows the blog titles to be read with an indication of content
    """
    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    """
    The Comment model allows users to leave a comment on a Blog Post
    It captures the users name and provides a trxt field for the comment
    It also allows the user to name their favourite Mod
    Admin have the ability to approve or remove any unsuitable comments
    The date and time of the comment are also captured and displayed
    """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="commenter")
    favourite_mod = models.CharField(max_length=100)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    """
    The Meta class orders the comments on the page
    """
    class Meta:
        ordering = ["-created_on"]

    """
    The __str__ method allows the comments to be read with an indication of content
    """

    def __str__(self):
        return f"Comment {self.body} by {self.author}"