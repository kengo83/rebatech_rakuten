from django.shortcuts import render,redirect
from .models import SearchModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
import os
import pprint
import pandas as pd
from .common import execute_api
from .rakutenAPI import rakuten_api
import requests
import json

class Create(CreateView):
    template_name = 'home.html'
    model = SearchModel
    fields = ('keyword','ng_keyword','sort','file','folda')
    success_url = reverse_lazy('result')

def resultfunc(request):
    for post in SearchModel.objects.all():
        keyword = post.keyword
        ng_keyword = post.ng_keyword
        sort = post.sort
        file = post.file
        folda = post.folda
    result = rakuten_api(keyword,ng_keyword,sort,file,folda)
    result_list = []
    picture_list = []
    for obj in result['Items']:
        picture_url = obj['Item']['mediumImageUrls'][0]
        picture_list.append(picture_url)
        title = obj['Item']['itemName']
        url = obj['Item']['itemUrl']
        result_list.append([title,url])
    pic_url = [p.get('imageUrl') for p in picture_list]
    context = {'list':result_list,'pic_list':pic_url}
    return render(request,'result.html',context)


    
    
