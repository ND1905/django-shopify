from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    posts=Blogpost.objects.all()
    n = len(posts)
    nSlides = n//2 + ceil((n/2)-(n//2))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'post': posts}

    return render(request, 'blog/bindex.html', params)

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})
    