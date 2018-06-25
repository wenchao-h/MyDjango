# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    print(posts)
    print(type(posts))
    post_lists = list()
    for count, post in enumerate(posts):
        print(type(count))
        print(type(post))
        print(post)
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    print(post_lists)
    return HttpResponse(post_lists)

