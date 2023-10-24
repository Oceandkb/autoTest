# @Time   ：2023/9/22 15:04
# @Author : Chao
# @File   : bbs_search_name.py

import allure
import requests
from requests import Response

# @allure.step("function description")
def bbs_search_name(s, base_url, id) -> Response:

    url = base_url + "/bbs-app/bbs/v1/invitation/detail/"+id+"?flag=0&sceneCode=5"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://aikn.iyunwen.com"
    from aikn_api.login_function import login
    login(s, base_url)
    i = 4049
    while i <= 4111:
        #print(i)
        i = i+2
        r = bbs_search_name(s, base_url, str(i))
        name = r.json()['data']['userName']
        print(name)