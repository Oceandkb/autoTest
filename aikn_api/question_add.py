# @Time   ：2023/9/6 9:22
# @Author : Chao
# @File   : question_add.py


import allure
import requests
from requests import Response

@allure.step("社区新增问题")
def question_add(s, base_url, question_title, question_content, plate_id) -> Response:
    '''

    :param s:
    :param base_url:
    :param question_title: str
    :param question_content: str
    :param plate_id: int
    :return:
    '''

    url = base_url + "/bbs-app/bbs/v1/invitation/add"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
            "title": question_title,
            "bbsType": 1,
            "content": question_content,
            "topics": [],
            "plateId": plate_id,
            "materialIds": [],
            "inviteUsers": []
        }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = question_add(login_fixture, base_url, question_title = '人类进化的主要驱动力是什么？',
                          question_content = '<p>人类进化的主要驱动力是什么？</p>', plate_id = 1265)
    print(result.text)