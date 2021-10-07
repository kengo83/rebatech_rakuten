from django.shortcuts import render,redirect
from .models import SearchModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
import os
import pprint
import pandas as pd
from .common import execute_api
from .rakutenAPI import rakuten_api, result_api
import requests
import json

class Create(CreateView):
    template_name = 'home.html'
    model = SearchModel
    fields = ('keyword','ng_keyword','sort','file','folda')
    success_url = reverse_lazy('csv')

def csvfunc(request):
    for post in SearchModel.objects.all():
        keyword = post.keyword
        ng_keyword = post.ng_keyword
        sort = post.sort
        file = post.file
        folda = post.folda
    rakuten_api(keyword,ng_keyword,sort,file,folda)
    return render(request,'home.html',{})

def resultfunc(request):
    for post in SearchModel.objects.all():
        keyword = post.keyword
        ng_keyword = post.ng_keyword
        sort = post.sort
    context = result_api(keyword,ng_keyword,sort)
    return render(request,'result.html',context)




    
    
