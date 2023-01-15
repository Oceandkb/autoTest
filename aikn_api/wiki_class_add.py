# conding = utf-8
# 新增分类
import time
import allure
import requests
import random
from requests import Response
# import os
timestamp1 = str(int(round(time.time()*1000)))

# @allure.title("添加分类成功")
def wiki_class_add(s, base_url)  -> Response:
    '''

    :param s:
    :param base_url:
    :param domainId: 知识类型id
    :param parentId: 分类的父分类id
    :return:
    '''
    # 函数定义之后的->，为定义的函数增加元数据，描述函数返回值的类型
    urlwclassadd = base_url + "/aikn-admin/knowledge/knowledge/v1/classes" + timestamp1
    r = requests.post(urlwclassadd)
    cookie1 = dict(r.cookies)
    s.cookies.update(cookie1)
    url = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"
    ran = str(random.randint(1,1000))
    wiki_class_name = "Auto_wiki_class" + ran
    body = {
        "domainId": 1,
        "name": wiki_class_name,
        "parentId": 0,
    }
    return s.post(url, json=body, cookies=cookie1) # res是通过发送post请求得到的返回数据，该post请求需要有json数据和登录cookie信息 返回respose内容

if __name__ == '__main__':
    s = requests.Session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login  # 执行login_function（不会执行if_name=='_main_':的代码）
    login(s, base_url)
    r = wiki_class_add(s, base_url)
    print(r.text)

# os.system("allure generate ./temp -o ./reports --clean")