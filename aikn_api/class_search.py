# @Time   ：2023/3/3 11:27
# @Author : Chao
# @File   : class_search.py

import allure
import requests
from requests import Response

@allure.step("搜索知识分类")
def class_search(s, base_url, domain_id) -> Response:
    """
    :return:
    :param s:
    :param base_url:
    :param kn_type:
    :param domain_id: 知识类型id，知识点：1 文库：2 视频：18 案例：19
    :return:
    """
    url = base_url + "/aikn-admin/unit/classes/v2/get?type=1&domainId=" + domain_id
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
    result = class_search(s, base_url, "18")
    print(result.text, type(result))