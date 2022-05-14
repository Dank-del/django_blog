from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Post

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html', {'title': 'about'})