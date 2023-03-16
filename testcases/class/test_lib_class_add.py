# @Time   ：2022/11/3 15:29
# @Author : Chao
# @File   : test_lib_class_add.py


import allure
from aikn_api.class_add import class_add
import requests

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("文库分类")
@allure.title("添加文库分类成功")
def test_lib_class_add(login_fixture, base_url, random_fixture):
    r = class_add(login_fixture, base_url, class_name= random_fixture("分类"), domain_id = 2)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'