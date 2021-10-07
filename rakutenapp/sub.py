from django.shortcuts import render
from .models import SearchModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
import os
import pandas as pd
from .common import execute_api
import requests
import json

EXP_CSV_PATH = "./{dir_name}/{csv_name}"
API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
ApplicationId = 1089791896465980338

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
    os.makedirs(folda,exist_ok=True)
    max_page = 10
    item_list = []
    for page in range(1,max_page+1):
        params = {
            'keyword' : keyword,
            "NGKeyword":ng_keyword,
            'applicationId': ApplicationId,
            'format':'json',
            'hits':30,
            'page':page,
            'sort':sort
        }
        res = execute_api(API_Endpoint, params)
        result = res.json()
        birth_list = ['itemName','itemPrice','itemCaption','itemUrl','postageFlag','shopName','shopCode','shopUrl']
        for i in range(0,len(result['Items'])):
            item_dict = {}
            elements = result['Items'][i]['Item']
            for key,value in elements.items():
                if key in birth_list:
                    item_dict[key] = value
            item_list.append(item_dict.copy())
        data = pd.DataFrame(item_list)
        data = data.reindex(columns=['itemName','itemPrice','itemUrl','itemCaption','postageFlag','shopName','shopCode','shopUrl'])
        data.columns = ['商品名', '値段', '商品url','商品説明','0:送料無し,1:送料あり','店舗名','店舗コード','店舗url']
        header = False if os.path.exists(EXP_CSV_PATH.format(dir_name=folda,csv_name=file))else True
        data.to_csv(EXP_CSV_PATH.format(dir_name=folda,csv_name=file),mode='a',index=False,header=header,encoding='utf_8_sig')
    result_list = []
    for obj in result['Items']:
        image = obj['Item']['mediumImageUrls']
        new_image = image['imageUrl']
        title = obj['Item']['itemName']
        url = obj['Item']['itemUrl']
        result_list.append([new_image,title,url])
    context = {'list':result_list,}
    return render(request,'result.html',context)


    
    
