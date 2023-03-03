# @Time   ：2022/11/3 14:58
# @Author : Chao
# @File   : test_lib_class_delete.py

import allure
from aikn_api.class_delete import class_delete
from aikn_api.class_search import class_search
import requests

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("文库分类")
@allure.title("删除文库分类成功")
def test_lib_class_delete(login_fixture, base_url):
    r1 = class_search(login_fixture, base_url, domain_id = str(2))
    r1_json = r1.json()
    id = str(r1_json['data'][0]['id'])
    name = str(r1_json['data'][0]['name'])
    if id == "-1":
        print("默认分类不允许删除！")
    else:
        r = class_delete(login_fixture, base_url, classes_id = id, domain_id = str(2))
        print(r.text)
        print(id, name)
        assert r.json()["code"] == 1
        assert r.status_code == 200
        assert r.json()['message'] == '分类删除成功'

