# @Time   ：2023/8/16 17:09
# @Author : Chao
# @File   : courseware_search.py

import allure
import requests
from requests import Response

@allure.step("课件查询")
def courseware_search(s, base_url, field_id) -> Response:
    '''

    :param s:
    :param base_url:
    :param field_id: 领域id, int型
    :return:
    '''

    url = base_url + "/knside-admin/exam/courseware/v1/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "pageSize": 10,
        "pageNum": 1,
        "data": {
            "coursewareName": "",
            "fieldIdList": [
                field_id
            ],
            "state": 3,
            "classesIdList": [],
            "addSearchLog": 1
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
    result = courseware_search(s, base_url, 251)
    print(result.text)
