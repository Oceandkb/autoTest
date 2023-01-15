# @Time   ：2022/11/18 14:43
# @Author : Chao
# @File   : test_entry_add.py

# import allure
# from aikn_api.entry_modify import entry_modify
# import requests
#
# @allure.epic("知识库")
# @allure.feature("词条")
# @allure.story("修改词条成功")
# def test_entry_modify(login_fixture, base_url):
#     r = entry_modify(login_fixture, base_url, entry_name, entry_id, entry_question_id)
#     print(r.text)
#     assert r.json()["code"] == 1
#     assert r.status_code == 200
#     assert r.json()['message'] == '操作成功!'
