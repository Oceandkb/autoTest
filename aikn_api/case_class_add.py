# # @Time   ：2023/3/3 9:46
# # @Author : Chao
# # @File   : case_class_add.py
#
#
# import allure
# import requests
# import random
# from requests import Response
#
#
# #ran = str(random.randint(1, 1000))
# @allure.step("新增案例库分类")
# def case_class_add(s, base_url, case_class_name) -> Response:
#
#     url = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"
#     h = {
#         "Accept": "application/json, text/plain, */*"
#     }
#     #kn_text_att_name = "Auto" + ran
#     body = {
#         "name": case_class_name,
#         "parentId": "0",
#         "domainId": 19
#     }
#
#     s.headers.update(h)
#     r = s.post(url, json=body)
#     return r
#
# if __name__ == '__main__':
#     s = requests.session()
#     base_url = "https://v6-stable.faqrobot.com.cn"
#     from aikn_api.login_function import login
#     login(s, base_url)
#     result = case_class_add(s, base_url, "售后案例")
#     print(result.text)
