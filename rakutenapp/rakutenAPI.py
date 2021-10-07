import requests
import os
from pprint import pprint
from .common import execute_api
from django.shortcuts import redirect
import numpy as np
import pandas as pd

def rakuten_api(keyword,ng_keyword,sort,file,folda):
    EXP_CSV_PATH = "./{dir_name}/{csv_name}"
    API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    ApplicationId = 1089791896465980338
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
        res = requests.get(API_Endpoint, params)
        result = res.json()
        pprint(result) # keyerror Itemsを防いでいる　なぜかわからない　後で質問する
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
    return result

# def result_api(keyword,ng_keyword,sort):
#     API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
#     ApplicationId = 1089791896465980338
#     max_page = 10
#     result_list = []
#     picture_list = []
#     for page in range(1,max_page+1):
#         params = {
#             'keyword' : keyword,
#             "NGKeyword":ng_keyword,
#             'applicationId': ApplicationId,
#             'format':'json',
#             'hits':30,
#             'page':page,
#             'sort':sort
#         }
#         res = requests.get(API_Endpoint, params)
#         result = res.json()
#         pprint(result) # keyerror Itemsを防いでいる　なぜかわからない　後で質問する
#         for obj in result['Items']:
#             picture_url = obj['Item']['mediumImageUrls'][0]
#             picture_list.append(picture_url)
#             title = obj['Item']['itemName']
#             url = obj['Item']['itemUrl']
#             result_list.append([title,url])
#         pic_url = [p.get('imageUrl') for p in picture_list]
#         context = {'list':result_list,'pic_list':pic_url}
#     return context


