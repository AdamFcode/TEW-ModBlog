from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    List Display dictates which fields to show on admin panel
    Search fields speeds up the search by limiting the search paramaters
    List filter allows superuser to filter by publication status
    Prepopulated fields helps automatically populate the slug with title content
    Summernote fields provides summernote functionality for greater editor features 
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)