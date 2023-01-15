# @Time   ：2022/11/3 14:58
# @Author : Chao
# @File   : test_lib_class_delet.py

import allure
from aikn_api.lib_class_delet import lib_class_delet
from aikn_api.lib_class_search import lib_class_search
import requests

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("文库分类")
@allure.title("删除文库分类成功")
def test_lib_class_delet(login_fixture, base_url):
    r1 = lib_class_search(login_fixture, base_url)
    r1_json = r1.json()
    lib_classesId = str(r1_json['data'][0]['id'])
    r = lib_class_delet(login_fixture, base_url, lib_classesId)
    print(r.text)

    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '分类删除成功'

