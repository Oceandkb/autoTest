# @Time   ：2023/3/3 9:34
# @Author : Chao
# @File   : api_demo.py

'''
import allure
import requests
from requests import Response

@allure.step("function description")
def function_name(s, base_url) -> Response:

    url = base_url + "api_url"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
           input parameters,
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = kn_tree_parent_att_add(s, base_url, 1335)
    print(result.text)

'''

