# @Time   ：2022/11/3 14:51
# @Author : Chao
# @File   : lib_class_delet.py

# Time：2022/10/11 9:59
# Author: chao
import requests
import allure
from requests import Response

@allure.step("删除文库分类")
def lib_class_delet(s, base_url, lib_classesId) ->Response:
    '''

    :param s:
    :param base_url:
    :param lib_classesId: 文库的分类Id
    :return:
    '''
    url=base_url+"/aikn-admin/knowledge/knowledge/v1/classes?classesId="+lib_classesId+"&domainId=2"
    r=requests.delete(url) #HTTP Delete
    js=r.json() #解析json（如果该接口响应的是content-type是json格式的数据）
    cookie1=r.cookies #获得cookie数据
    res=s.delete(url, json=js, cookies=cookie1)
    return res

if __name__=='__main__':
    base_url="https://v5-test.faqrobot.cn"
    from api.login_function import login
    login(s,base_url)
    result=lib_class_delet(s,base_url)
    print(result.text)