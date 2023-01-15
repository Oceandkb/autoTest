'''
import allure
from api.robot_function import robotInt
import requests


@allure.title('问答')
def test_robot_1(base_url):
    """问答"""
    s = requests.Session()
    r = robotInt(s, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert len(r.json()["data"]["robotResults"]) > 0
    assert r.json()['message'] == '请求成功!'


@allure.title('访客不存在')
def test_robot_2(base_url):
    """访客不存在"""
    s = requests.Session()
    r = robotInt(s, base_url, sourceId="16666")
    print("\n", r.text)
    assert r.json()["code"] == -100
    assert r.json()["message"] == "访客不存在!"


@allure.title('站点不存在')
def test_robot_3(base_url):
    """站点不存在"""
    s = requests.Session()
    r = robotInt(s, base_url, sysNum="16456806328271")
    print("\n", r.text)
    assert r.json()["code"] == 0
    assert r.json()["message"] == "站点不存在!"
'''