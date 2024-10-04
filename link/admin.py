from django.contrib import admin
from .models import Link
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Link)
class LinkAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
