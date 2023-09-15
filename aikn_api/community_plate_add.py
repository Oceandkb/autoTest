# @Time   ：2023/9/15 17:30
# @Author : Chao
# @File   : community_plate_add.py

import allure
import requests
from requests import Response

@allure.step("新增社区版块")
def community_plate_add(s, base_url, plate_name) -> Response:
    '''

    :param s:
    :param base_url:
    :param plate_name: 版块名称  str
    :return:
    '''

    url = base_url + "/knside-admin/bbs/plate/v1/add"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
           "name": plate_name
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