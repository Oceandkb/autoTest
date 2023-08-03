# @Time   ：2022/11/18 14:52
# @Author : Chao
# @File   : entry_delete.py

import allure
import requests
from requests import Response

@allure.step("删除词条")
def entry_delete(s, base_url, entry_id) -> Response:
    '''

    :param s:
    :param base_url:
    :param entry_id: 词条id
    :return:
    '''

    url = base_url + "/aikn-admin/knowledge/knowledge/v1/recycle-bin/approve"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    body = {
        "knowledgeId": entry_id,
        "approveType": 1,
        "approveUserIds": []
    }
    s.headers.update(h)
    r = s.post(url, json = body)
    #r_json = return ()
    return r



if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    entry_delete(s, base_url)
    result = entry_delete(s, base_url)
    print(result.text)