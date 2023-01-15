# @Time   ：2022/11/8 14:26
# @Author : Chao
# @File   : wiki_class_search.py


import allure
import requests
from requests import Response

@allure.step("百科分类查询")
def wiki_class_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/unit/classes/v2/get?type=1&domainId=1"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    #r_json = r.json()
    return r



if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    wiki_class_search(s, base_url)
    result = wiki_class_search(s, base_url)
    print(result.text)
