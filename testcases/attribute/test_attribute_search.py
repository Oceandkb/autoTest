# @Time   ：2022/11/4 14:46
# @Author : Chao
# @File   : test_attribute search.py

import allure
import requests
from aikn_api.kn_att_search import kn_all_att_search

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('查询知识属性成功')
# @pytest.mark.smoke
def test_kn_all_att_search(login_fixture, base_url):
    r = kn_all_att_search(login_fixture, base_url)
    if r == None:
        print(r)
    else:
        assert r.json()["code"] == 1
        assert r.status_code == 200
        assert r.json()['message'] == '操作成功!'
