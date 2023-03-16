# @Time   ：2023/3/3 11:15
# @Author : Chao
# @File   : test_video_class_add.py

import allure
from aikn_api.class_add import class_add
import requests

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("视频库分类")
@allure.title("添加案例分类成功")
def test_case_class_add(login_fixture, base_url, random_fixture):
    r = class_add(login_fixture, base_url, class_name= random_fixture("分类"), domain_id = 18)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'