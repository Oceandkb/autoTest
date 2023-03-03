# @Time   ：2022/11/3 15:11
# @Author : Chao
# @File   : test_wiki_class_add.py
import allure
from aikn_api.class_add import class_add
import requests

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("百科分类")
@allure.title("添加百科分类成功")
def test_wiki_class_add(login_fixture, base_url):
    r = class_add(login_fixture, base_url, class_name= random_fixture, domain_id = 1)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'