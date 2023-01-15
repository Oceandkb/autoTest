# @Time   ：2022/11/8 14:09
# @Author : Chao
# @File   : test_lib_class_search.py


import allure
import requests
from aikn_api.wiki_class_search import wiki_class_search

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("百科分类")
@allure.title('查询百科分类成功')
# @pytest.mark.smoke
def test_wiki_class_search(login_fixture, base_url):
    r = wiki_class_search(login_fixture, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'