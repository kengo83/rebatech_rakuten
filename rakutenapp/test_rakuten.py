from .rakutenAPI import rakuten_api
import pprint

def test_rakutenAPI():
    keyword = '牛肉'
    ng_keyword = 'kg 切り落とし'
    sort = 'standard'
    file = 'yaruo.csv'
    folda = 'yaruo'
    result = rakuten_api(keyword,ng_keyword,sort,file,folda)

    assert result['Items'][0]['Item']['itemName']
    assert result['Items'][0]['Item']['itemPrice']
