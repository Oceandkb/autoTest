# @Time   ：2022/11/15 16:13
# @Author : Chao
# @File   : test_kn_att_wiki_class_cite.py

'''
import allure
import requests
from aikn_api.kn_att_wiki_class_cite import kn_att_wiki_class_cite
from aikn_api.kn_att_search import kn_all_att_search


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('百科分类知识属性引用成功')
#@pytest.mark.smoke
def test_kn_att_wiki_class_cite(login_fixture, base_url):
    r1 = kn_all_att_search(login_fixture, base_url)
    r1_json = r1.json()
    cite_att_id = str(r1_json['data']['list'][0]['id'])
    print(public_cite_att_id)
    r = kn_att_wiki_class_cite(login_fixture, base_url, cite_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
'''