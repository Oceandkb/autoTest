# @Time   ：2023/3/16 9:33
# @Author : Chao
# @File   : test_case_add.py

import allure
import pytest

from aikn_api.case_add import case_add
import requests

@allure.epic("知识库")
@allure.feature("知识")
@allure.story("案例库")
@allure.title("新增富文本案例成功")
@pytest.mark.parametrize('classId_search_fixture', ['19'], indirect = True)
def test_case_add(login_fixture, base_url, datetime_fixture, field_search_fixture, classId_search_fixture):
    r = case_add(login_fixture, base_url, case_name = datetime_fixture + "案例", rich_text_content = "", edit_type = "1",
                 class_id = classId_search_fixture, field_id = field_search_fixture,
                 open_field_id = field_search_fixture, markdown_content = "于" + datetime_fixture + "编写")
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'