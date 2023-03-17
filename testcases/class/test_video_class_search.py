# @Time   ：2023/3/3 14:21
# @Author : Chao
# @File   : test_video_class_search.py

import allure
import requests
from aikn_api.class_search import class_search

@allure.epic("知识库")
@allure.feature("分类")
@allure.story("视频库分类")
@allure.title('查询视频库分类成功')
# @pytest.mark.smoke
def test_video_class_search(login_fixture, base_url):
    r = class_search(login_fixture, base_url, domain_id = str(18))
    print(r.text)
    #for x in r_text:
     #   print(x)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'