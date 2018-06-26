# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

#def homepage(request):
#    posts = Post.objects.all()
#    post_lists = list()
#    for count, post in enumerate(posts):
#        post_lists.append("No.{} ".format(str(count)) +post.title+"<hr>")
#        post_lists.append("<small>" + post.body + "</small><br></br>")        
#    return HttpResponse(post_lists)

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
