# @Time   ：2022/11/4 13:40
# @Author : Chao
# @File   : test_kn_att_del.py

'''
import allure
import requests
from aikn_api.kn_att_delete import kn_all_att_delete
from aikn_api.kn_att_search import kn_all_att_search


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('删除知识属性成功')
#@pytest.mark.smoke
def test_kn_all_att_delete(login_fixture, base_url):
    r1 = kn_att_search(login_fixture, base_url)
    r1_json = r1.json()
    kn_att_id = str(r1_json['data']['list'][1]['id'])
    r = kn_att_delete(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

'''