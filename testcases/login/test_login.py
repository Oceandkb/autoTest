# import pytest
# import os

import allure
from aikn_api.login_function import login
import requests

@allure.feature("登录")
@allure.story("门户首页登录")
@allure.title("登录成功")
def test_login_1(base_url):
    s = requests.Session()
    r = login(s, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '登录成功!'
'''
@allure.title("登录失败")
def test_login_2(base_url="https://v5-test.faqrobot.cn"):
    """输入正确账号密码登录成功"""
    s = requests.Session()
    r = login(s, base_url,user="test", password="123456")
    print(r.text)
    assert r.json()["code"] == -3
    assert r.status_code == 200
    assert r.json()['message'] == '用户名或密码错误'


@allure.title('错误账号登录')
def test_login_2(base_url):
    """输入错误的账号，登录失败"""
    s = requests.Session()
    r = login(s, base_url, user='test', password="123456")
    print("\n", r.text)
    assert r.json()["code"] == -4
    assert r.json()["message"] == "Incorrect username or password"
'''
