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
from aikn_api.field_search import field_search
from aikn_api.check_att_reference import check_att_reference

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('文本知识属性新增成功')
# @pytest.mark.smoke
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
# @pytest.mark.smoke
def test_kn_att_modify(login_fixture, base_url):
    r_search = kn_all_att_search(login_fixture, base_url)
    if r_search == None:
        print(r_search)
    else:
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
# @pytest.mark.smoke
def test_kn_att_public_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
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
# @pytest.mark.smoke
def test_public_kn_att_disabled(login_fixture, base_url):
    r1 = kn_public_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
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
# @pytest.mark.smoke
def test_public_kn_att_delete(login_fixture, base_url):
    r1 = kn_public_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
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
# @pytest.mark.smoke
def test_kn_att_wiki_class_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
        r1_json = r1.json()
        cite_att_id = str(r1_json['data']['list'][0]['id'])
        print(cite_att_id)
        r = kn_att_wiki_class_cite(login_fixture, base_url, cite_att_id)
        print(r.text)
        assert r.json()["code"] == 1
        assert r.json()['message'] == '操作成功!'


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('禁用百科分类关联的知识属性成功')
# @pytest.mark.smoke
def test_wiki_class_kn_att_disabled(login_fixture, base_url):
    r1 = kn_wiki_class_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
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
# @pytest.mark.smoke
def test_wiki_class_kn_att_delete(login_fixture, base_url):
    r1 = kn_wiki_class_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
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
# @pytest.mark.smoke
def test_field_kn_att_public_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    if r1 == None:
        print(r1)
    else:
        r1_json = r1.json()
        cite_att_id = str(r1_json['data']['list'][0]['id'])
        _r_ = field_search(login_fixture, base_url)
        field_id = str(_r_.json()['data'][0]['id'])
        r = kn_att_field_cite(login_fixture, base_url, cite_att_id, field_id)
        print(r.text)
        assert r.json()["code"] == 1
        assert r.status_code == 200
        assert r.json()['message'] == '操作成功!'


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('切换领域关联的知识属性成功')
# @pytest.mark.smoke
def test_field_kn_att_disabled(login_fixture, base_url):
    r0 = field_search(login_fixture, base_url)
    field_id = r0.json()['data'][0]['id']
    r1 = kn_field_att_search(login_fixture, base_url, field_id)
    if r1 == None:
        print(r1)
    else:
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
@allure.title('删除默认领域关联的知识属性成功')
# @pytest.mark.run(order=11)
# @pytest.mark.smoke
def test_field_kn_att_delete(login_fixture, base_url):
    r0 = field_search(login_fixture, base_url)
    field_id = str(r0.json()['data'][0]['id'])
    print("默认领域的id为：" + field_id)
    r1 = kn_field_att_search(login_fixture, base_url, field_id)
    # 判断默认领域关联的知识属性列表是否为空，为空则打印列表为空，不为空执行else部分
    if r1 == None:
        print(r1)
    else:
        kn_field_att_id = str(r1.json()['data']['list'][0]['id'])
        if r1.json()['data']['list'][0]['status'] == 1:
            r2 = field_kn_att_disabled(login_fixture, base_url, kn_field_att_id)
            print(r2.text)
            r = kn_field_att_delete(login_fixture, base_url, kn_field_att_id)
            print(r.text)
            assert r.json()["code"] == 1
            assert r.status_code == 200
            assert r.json()['message'] == '操作成功!'
        else:
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
# @pytest.mark.run(order=12)
# @pytest.mark.smoke
def test_kn_all_att_delete(login_fixture, base_url):
    r0 = kn_all_att_search(login_fixture, base_url)
    # 判断所有知识属性列表是否为空，为空，则输出提示；否则，执行else
    if r0 == None:
        print(r1)
    else:
        kn_att_id = str(r0.json()['data']['list'][0]['id'])
        r1 = check_att_reference(login_fixture, base_url, kn_att_id)
        # 判断属性是否被引用，如果被引用，提示；否则，执行删除
        # 这里没有做取消引用， 因为比较复杂， 要判断check_att_reference接口返回的data中的值是多少，然后根据值去找被应用的位置，再执行解绑
        if len(r1.json()["data"]) > 0:
            print("该属性已被引用，无法删除")
        else:
            r = kn_all_att_delete(login_fixture, base_url, kn_att_id)
            print(r.text)
            assert r.json()["code"] == 1
            assert r.status_code == 200
            assert r.json()['message'] == '操作成功!'
