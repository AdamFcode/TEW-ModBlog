from django.shortcuts import render, get_object_or_404
from .models import Link


def link_list(request):
    """
    Renders the Link page
    """
    queryset = Link.objects.all()
    link = get_object_or_404(queryset)

    return render(
        request,
        "link/link.html",
        {"link": link,},
    )
