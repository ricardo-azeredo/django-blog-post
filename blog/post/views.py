from django.shortcuts import render

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts })

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")