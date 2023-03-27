# @Time   ：2023/3/16 9:33
# @Author : Chao
# @File   : test_case_add.py

import allure
from aikn_api.case_add import case_add
from aikn_api.class_search import class_search
from aikn_api.field_search import field_search
import requests

@allure.epic("知识库")
@allure.feature("知识")
@allure.story("案例库")
@allure.title("新增富文本案例成功")
def test_case_add(login_fixture, base_url, random_fixture):

    r1 = class_search(login_fixture, base_url, domain_id=str(19)).json()
    _class_id_ = str(r1['data'][0]['id'])
    r2 = field_search(login_fixture, base_url).json()
    _field_id_ = str(r2['data'][0]['id'])
    _open_field_id_ = str(r2['data'][0]['id'])
    r = case_add(login_fixture, base_url, case_name = random_fixture("案例"), rich_text_content = "", edit_type = "1",
                 class_id = _class_id_, field_id = _field_id_, open_field_id = _open_field_id_, markdown_content = random_fixture("内容"))
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'