# @Time   ：2023/3/16 13:27
# @Author : Chao
# @File   : field_search.py


import allure
import requests
from requests import Response

@allure.step("搜索知识领域")
def field_search(s, base_url) -> Response:
    """

    :param s:
    :param base_url:
    :return:
    """
    url = base_url + "/aikn-admin/knowledge/field/v1/field"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    return r



if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = field_search(s, base_url)
    print(result.text)