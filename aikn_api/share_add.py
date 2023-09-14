# @Time   ：2023/9/12 17:14
# @Author : Chao
# @File   : share_add.py


import allure
import requests
from requests import Response

@allure.step("新增分享")
def share_add(s, base_url, share_title, share_content, plate_id, class_id) -> Response:
    '''

    :param s:
    :param base_url:
    :param share_title: 分享名称 str
    :param share_content: 分享内容 str
    :param plate_id: 模块id int
    :param class_id: 分类id str
    :return:
    '''

    url = base_url + "/bbs-app/bbs/v1/invitation/add"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
    "title": share_title,
    "plateId": plate_id,
    "bbsType": 2,
    "caseClassesIds": [
        class_id
    ],
    "content": share_content,
    "coverPicPath": "",
    "materialIds": [],
    "topics": []
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = share_add(s, base_url, share_title='test', share_content='<p>test</p>', plate_id=1235, class_id='-1')
    print(result.text)
