# @Time   ：2022/11/4 13:40
# @Author : Chao
# @File   : kn_att_delete.py

'''知识属性删除接口，包括知识属性的彻底删除，以及从公共属性、关联分类和领域属性的解除'''

import requests
import allure
from requests import Response
from aikn_api.kn_att_search import kn_all_att_search
from aikn_api.kn_att_search import kn_public_att_search

@allure.step("删除知识属性")
def kn_all_att_delete(s, base_url, kn_att_id) ->Response:
    '''
    删除知识属性
    :param s:
    :param base_url:
    :param kn_att_id: 删除的知识属性id
    :return:
    '''
    url=base_url+"/aikn-admin/knowledge/v1/dynamic-label/"+kn_att_id
    r=requests.delete(url) # HTTP Delete
    cookie1=r.cookies# 获得cookie数据
    res=s.delete(url, json=r.json(), cookies=cookie1)


    return res


@allure.step("删除公共属性关联的知识属性")
def kn_public_att_delete(s, base_url, kn_public_att_id) ->Response:
    '''

    :param s:
    :param base_url:
    :param kn_public_att_id: 删除的公共属性关联的知识属性id
    :return:
    '''
    url=base_url+"/aikn-admin/knowledge/field/v1/field-label/"+kn_public_att_id
    r=requests.delete(url) # HTTP Delete
    cookie1=r.cookies# 获得cookie数据
    return s.delete(url, json = r.json(), cookies = cookie1)

@allure.step("删除百科分类关联的知识属性")
def kn_wiki_class_att_delete(s, base_url, kn_wiki_class_att_id) ->Response:
    '''

    :param s:
    :param base_url:
    :param kn_class_att_id: 删除的百科分类关联的知识属性id
    :return:
    '''
    url= base_url +"/aikn-admin/knowledge/classes-label/v1/delete/" + kn_wiki_class_att_id
    r=requests.get(url) # HTTP Delete
    cookie1=r.cookies# 获得cookie数据
    res=s.get(url, json = r.json(), cookies=cookie1)
    return res

@allure.step("删除领域关联的知识属性")
def kn_field_att_delete(s, base_url, kn_field_att_id) ->Response:
    '''

    :param s:
    :param base_url:
    :param kn_field_att_id: 删除的领域关联的知识属性id
    :return:
    '''
    url= base_url +"/aikn-admin/knowledge/field/v1/field-label/" + kn_field_att_id
    r=requests.delete(url) # HTTP Delete
    cookie1=r.cookies# 获得cookie数据
    res=s.delete(url, json = r.json(), cookies=cookie1)
    return res

'''
if __name__=='__main__':
    s=requests.session()
    base_url="https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result=kn_att_delete(s, base_url)
    print(result.text)
'''