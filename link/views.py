from django.shortcuts import render
from django.views import generic
from .models import Link


# Requests and returns links and blurbs for the link section
def link(request):
    link = Link.objects.all()
    return render(request, 'link/link.html', {"link": link})
