# @Time   ：2022/11/8 14:03
# @Author : Chao
# @File   : lib_class_search.py


import allure
import requests
from requests import Response

@allure.step("搜索文库分类")
def lib_class_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/unit/classes/v2/get?type=1&domainId=2"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    return r



if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from api.login_function import login
    login(s, base_url)
    lib_class_search(s, base_url)
    result = lib_class_search(s, base_url)
    print(result.text)
