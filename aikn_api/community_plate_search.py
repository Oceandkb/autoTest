# @Time   ：2023/9/8 17:47
# @Author : Chao
# @File   : community_plate_search.py



import allure
import requests
from requests import Response

@allure.step("社区版块查询")
def community_plate_search(s, base_url) -> Response:

    url = base_url + "/knside-admin/bbs/plate/v1/query/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "pageNum":1,
        "pageSize":10,
        "data":{
            "name":"",
            "sortType":1
        }
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    # base_url = "https://v6-stable.faqrobot.com.cn"
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = community_plate_search(s, base_url)
    print(result.text)
