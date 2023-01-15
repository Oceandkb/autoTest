# @Time   ：2022/11/15 14:52
# @Author : Chao
# @File   : test_kn_att_public_cite.py

import allure
import requests
from aikn_api.kn_att_cite import kn_att_public_cite
from aikn_api.kn_att_search import *



@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('公共知识属性引用成功')
#@pytest.mark.smoke
def test_kn_att_public_cite(login_fixture, base_url, kn_att_fixture):
    #r1 = kn_att_search(login_fixture, base_url)
    #r1_json = r1.json()
    #cite_att_id = str(r1_json['data']['list'][0]['id'])
    #print(cite_att_id)
    r = kn_att_public_cite(login_fixture, base_url, kn_att_fixture)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
