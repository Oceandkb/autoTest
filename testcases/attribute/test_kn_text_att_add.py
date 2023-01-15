# @Time   ：2022/11/3 14:07
# @Author : Chao
# @File   : test_kn_att_add_tree.py


import allure
import requests
import pytest
from aikn_api.kn_att_add import kn_text_att_add
from aikn_api.kn_att_modify import kn_att_modify

# @allure.epic("知识库")
# @allure.feature("属性")
# @allure.story("知识属性")
# @allure.title('新增文本知识属性成功')
# #@pytest.mark.smoke
# def test_kn_text_att_add(login_fixture, base_url, random_fixture):
#     r = kn_text_att_add(login_fixture, base_url, random_fixture)
#     print(r.text)
#     assert r.json()["code"] == 1
#     assert r.status_code == 200
#     assert r.json()['message'] == '操作成功!'
