# @Time   ：2022/11/15 16:22
# @Author : Chao
# @File   : test_kn_att.py

import allure
import requests
import pytest
import random
from aikn_api.kn_att_add import kn_text_att_add
from aikn_api.kn_att_modify import kn_att_modify
from aikn_api.kn_att_cite import *
from aikn_api.kn_att_search import *
from aikn_api.kn_att_modify import kn_att_modify
from aikn_api.kn_att_delete import *
from aikn_api.kn_att_disabled import *

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('文本知识属性新增成功')
@pytest.mark.run(order = 1)
#@pytest.mark.smoke
def test_kn_text_att_add(login_fixture, base_url, random_fixture):
    r = kn_text_att_add(login_fixture, base_url, random_fixture("文本"))
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('修改知识属性成功')
@pytest.mark.run(order = 2)
#@pytest.mark.smoke
def test_kn_att_modify(login_fixture, base_url):
    r_search = kn_all_att_search(login_fixture, base_url)
    r_search_json = r_search.json()
    kn_att_id = r_search_json['data']['list'][0]['id']
    r = kn_att_modify(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('公共知识属性引用成功')
@pytest.mark.run(order = 3)

#@pytest.mark.smoke
def test_kn_att_public_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    r1_json = r1.json()
    cite_att_id = str(r1_json['data']['list'][0]['id'])
    print(cite_att_id)
    r = kn_att_public_cite(login_fixture, base_url, cite_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('禁用公共知识属性成功')
@pytest.mark.run(order = 4)
#@pytest.mark.smoke
def test_public_kn_att_disabled(login_fixture, base_url):
    r1 = kn_public_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_att_id = str(r1_json['data']['list'][0]['id'])
    r = public_kn_att_disabled(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('公共属性删除知识属性成功')
@pytest.mark.run(order = 5)
#@pytest.mark.smoke
def test_public_kn_att_delete(login_fixture, base_url):
    r1 = kn_public_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_public_att_id = str(r1_json['data']['list'][0]['id'])
    r = kn_public_att_delete(login_fixture, base_url, kn_public_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

'''
百科分类关联知识属性、禁用和解除关联
'''
@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('百科分类关联知识属性成功')
@pytest.mark.run(order = 6)

#@pytest.mark.smoke
def test_kn_att_wiki_class_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    r1_json = r1.json()
    cite_att_id = str(r1_json['data']['list'][0]['id'])
    print(cite_att_id)
    r = kn_att_wiki_class_cite(login_fixture, base_url, cite_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('禁用百科分类关联的知识属性成功')
@pytest.mark.run(order = 7)
#@pytest.mark.smoke
def test_wiki_class_kn_att_disabled(login_fixture, base_url):
    r1 = kn_wiki_class_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_att_id = str(r1_json['data']['list'][0]['id'])
    r = wiki_class_kn_att_disabled(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('删除百科分类关联的知识属性成功')
@pytest.mark.run(order = 8)
#@pytest.mark.smoke
def test_wiki_class_kn_att_delete(login_fixture, base_url):
    r1 = kn_wiki_class_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_wiki_class_att_id = str(r1_json['data']['list'][0]['id'])
    r = kn_wiki_class_att_delete(login_fixture, base_url, kn_wiki_class_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

'''
领域关联知识属性、禁用和解除关联
'''

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('领域关联知识属性成功')
@pytest.mark.run(order = 9)
#@pytest.mark.smoke
def test_field_kn_att_public_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    r1_json = r1.json()
    cite_att_id = str(r1_json['data']['list'][0]['id'])
    #print(cite_att_id)
    r = kn_att_field_cite(login_fixture, base_url, cite_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('禁用领域关联的知识属性成功')
@pytest.mark.run(order = 10)
#@pytest.mark.smoke
def test_field_kn_att_disabled(login_fixture, base_url):
    r1 = kn_field_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_field_att_id = str(r1_json['data']['list'][0]['id'])
    r = field_kn_att_disabled(login_fixture, base_url, kn_field_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('删除领域关联的知识属性成功')
@pytest.mark.run(order = 11)
#@pytest.mark.smoke
def test_field_kn_att_delete(login_fixture, base_url):
    r1 = kn_field_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_field_att_id = str(r1_json['data']['list'][0]['id'])
    r = kn_field_att_delete(login_fixture, base_url, kn_field_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

'''
删除知识属性
'''
@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('删除知识属性成功')
@pytest.mark.run(order = 12)
#@pytest.mark.smoke
def test_kn_all_att_delete(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_att_id = str(r1_json['data']['list'][0]['id'])
    r = kn_all_att_delete(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'



