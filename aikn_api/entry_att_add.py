import requests
import allure
import random
from requests import Response

@allure.step("新增词条属性")
def entry_att_add(s, base_url) ->Response:
    '''
    新增词条属性
    :param s:
    :param base_url:
    :return:
    '''
    url = base_url+"/aikn-admin/knowledge/knowledge/v1/attribute/add"
    ran = str(random.randint(1,1000))  #生成随机数
    entry_att = "自动化-词条属性" + ran  #词条
    body = {
        "name": entry_att
    }
    h = {
            "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r= s.post(url, json=body)
    return r



if __name__ == '__main__':
    s=requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = entry_att_add(s, base_url)
    print(result.text)
