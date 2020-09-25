from django.shortcuts import render, get_object_or_404
from.models import BlogEntry


def allblogs(request):
    blogs = BlogEntry.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blogdetail= get_object_or_404(BlogEntry, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blogdetail}, {'blog_id': blog_id})


