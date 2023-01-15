# @Time   ：2022/11/18 14:43
# @Author : Chao
# @File   : test_entry_add.py

# import allure
# from aikn_api.entry_add import entry_add
# import requests
#
# @allure.epic("知识库")
# @allure.feature("词条")
# @allure.story("新增词条成功")
# def test_entry_add(login_fixture, base_url, random_fixture):
#     r = entry_add(login_fixture, base_url, random_fixture)
#     print(r.text)
#     assert r.json()["code"] == 1
#     assert r.status_code == 200
#     assert r.json()['message'] == '操作成功!'
