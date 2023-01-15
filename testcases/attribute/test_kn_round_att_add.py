# @Time   ：2022/11/3 16:41
# @Author : Chao
# @File   : test_kn_attribute_add2.py

import allure
import requests
import pytest
import random
from aikn_api.kn_att_add import kn_day_att_add

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('新增时间-周期知识属性成功')
#@pytest.mark.smoke
def test_kn_round_att_add(login_fixture, base_url):
    vs = 6
    ran = str(random.randint(1,1000))
    time_name = "Auto_round" + ran
    r = kn_day_att_add(login_fixture, base_url, vs, time_name)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
