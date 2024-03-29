from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Dusnazarov Elyor',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'Mart 28, 2024'

    },
     {
        'author':'Core Shafer',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'Mart 29, 2024'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


