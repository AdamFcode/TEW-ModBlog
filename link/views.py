from django.shortcuts import render
from .models import Link


def link(request):
    """
    Renders the Link page
    """
    link = Link.objects.all()

    return render(
        request,
        "link/link.html",
        {"link": link},
    )