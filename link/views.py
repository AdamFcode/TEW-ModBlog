from django.shortcuts import render
from .models import Link


def link_list(request):
    """
    Renders the Link page
    """
    link_list = Link.objects.all()

    return render(
        request,
        "link/link.html",
        {"links": Link},
    )