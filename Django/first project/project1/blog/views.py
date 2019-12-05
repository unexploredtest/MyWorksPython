from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

comments = [

    {

    "title": "First Post!",
    "author": "aliPMPAINT",
    "date": "2019/11/15",
    "content": "First awesome post in this incredible website!"

    },

    {

    "title": "Second Post!",
    "author": "MRSawari",
    "date": "2019/11/16",
    "content": "Second awesome post in this incredible website!"

    },

    {

    "title": "Third Post!",
    "author": "Dr.sawari",
    "date": "2019/11/17",
    "content": "Third awesome post in this incredible website!"

    }
]

def home(request):
    context = { "comments": Post.objects.all()}

    return render(request, "blog/home.html", context)

def about(request):

    return render(request, "blog/about.html", {"title": "about"})
