from django.shortcuts import render

from .models import Post

def listar_posts(request):
    posts = Post.objects.all().order_by('-data_de_criacao')
    return render(request, 'blog/listar_posts.html', {'posts': posts})