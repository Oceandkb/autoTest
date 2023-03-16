# @Time   ：2022/11/3 14:19
# @Author : Chao
# @File   : test_kn_att_add0.py

import allure
import requests
import pytest
from aikn_api.kn_att_add import kn_tree_parent_att_add
from aikn_api.kn_att_add import kn_tree_kids_att_add


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('新增树型知识属性成功')
#@pytest.mark.smoke
def test_kn_tree_parent_att_add(login_fixture, base_url, random_fixture):
    r1 = kn_tree_parent_att_add(login_fixture, base_url, random_fixture("parents"))
    r2 = kn_tree_kids_att_add(login_fixture, base_url, random_fixture("kids"))
    print(r1.text)
    print(r2.text)
    assert r2.json()["code"] == 1
    assert r2.status_code == 200
    assert r2.json()['message'] == '操作成功!'