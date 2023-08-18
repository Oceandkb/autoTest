# @Time   ：2023/8/16 13:57
# @Author : Chao
# @File   : material_search.py

import allure
import requests
from requests import Response

@allure.step("素材检索")
def material_search(s, base_url, material_type) -> Response:
    '''

    :param s:
    :param base_url:
    :param material_type: 素材的类型，str
    :return:
    '''

    url = base_url + "/admin/public/file/v1/material/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
            "pageNum": 1,
            "pageSize": 10,
            "data": {
                "classesId": "",
                "type": material_type
            }
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = material_search(s, base_url, "1")
    print(result.text)
