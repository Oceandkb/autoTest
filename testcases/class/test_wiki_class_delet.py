import allure
from aikn_api.wiki_class_delet import wiki_class_delet
from aikn_api.wiki_class_search import wiki_class_search
import requests


@allure.epic("知识库")
@allure.feature("分类")
@allure.story("百科分类")
@allure.title("删除百科分类成功")
def test_wiki_class_delet(login_fixture, base_url):
    r1 = wiki_class_search(login_fixture, base_url)
    r1_json = r1.json()
    classesId = str(r1_json['data'][0]['id'])
    r = wiki_class_delet(login_fixture, base_url, classesId)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '分类删除成功'


