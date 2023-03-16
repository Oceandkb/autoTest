# @Time   ：2023/1/12 17:15
# @Author : Chao
# @File   : test_gather_task_add_required.py



import allure
import requests
import random
import pytest
from aikn_api.gather_task_add import gather_task_add_required

@allure.epic("知识库")
@allure.feature("采编任务")
@allure.story("新增采编任务-必填项")
def test_gather_task_add_required(login_fixture, base_url, random_fixture):
    r = gather_task_add_required(login_fixture, base_url, task_name = random_fixture("任务"))
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
