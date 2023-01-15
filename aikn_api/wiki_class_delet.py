# Time：2022/10/11 9:59
# Author: chao
import requests
import allure
from requests import Response

def wiki_class_delet(s, base_url, classesId) ->Response:
    '''

    :param s:
    :param base_url:
    :param classesId:
    :return:
    '''
    url=base_url+"/aikn-admin/knowledge/knowledge/v1/classes?classesId="+classesId+"&domainId=1"
    r=requests.delete(url) # HTTP Delete
    js=r.json() # 解析json（如果该接口响应的是content-type是json格式的数据）
    cookie1=r.cookies# 获得cookie数据
    res=s.delete(url, json=js, cookies=cookie1)
    return res
#--------------------------------------------------------------------------------------------
if __name__=='__main__':
    s=requests.session()
    base_url="https://v5-test.faqrobot.cn"
    from api.login_function import login
    login(s,base_url)
    result=wiki_class_delet(s, base_url)
    print(result.text)