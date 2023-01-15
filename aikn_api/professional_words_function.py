import requests
from requests import Response
import datetime


def add_words(s, base_url, word_name, word_type="1", **kwargs) -> Response:
    """添加词库"""
    word_url1 = base_url + "/admin/qaknowledge/wordDoc/v1/wordDoc"
    body = {
        "nature": 0,
        "nominal": 0,
        "type": word_type,
        "word": word_name,
        "weight": 0
    }
    body.update(kwargs)
    word_res = s.post(word_url1, json=body)
    return word_res


def update_words(s, base_url, new_word_name,
                 word_id=None, word_type="1", **kwargs) -> Response:
    word_url1 = base_url + "/admin/qaknowledge/wordDoc/v1/wordDoc"
    body = {
        "nature": 0,
        "nominal": 0,
        "type": word_type,
        "word": new_word_name,
        "id": word_id,
        "weight": 0
    }
    body.update(kwargs)
    return s.put(word_url1, json=body)


def get_words(s, base_url, word_type="1", pageNum=1, pageSize=10) -> Response:
    word_url1 = base_url + "/admin/qaknowledge/wordDoc/v1/wordDoc/list"
    body = {
        "data": {
            "key": "",
            "type": word_type,
            "weight": [],
            "nature": [],
            "nominal": []
        },
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    return s.post(word_url1, json=body)


def detele_words(s, base_url, word_id=None) -> Response:
    word_url1 = base_url + "/admin/qaknowledge/wordDoc/v1/wordDoc/{}/1".format(word_id)
    return s.delete(word_url1)


if __name__ == '__main__':
    s = requests.Session()
    base_url = "https://v5-test.faqrobot.cn"
    from api.login_function import login

    login(s, base_url)
    word_name = "专业名词" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    r1 = add_words(s, base_url, word_name)
    print(r1.text)
    r2 = get_words(s, base_url)
    print(r2.json()["data"]["list"][0])
    print(r2.json()["data"]["list"][0]["id"])
    word_id = r2.json()["data"]["list"][0]["id"]
    new_word_name = "修改的名词" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    r3 = update_words(s, base_url, new_word_name, word_id)
    print(r3.text)
