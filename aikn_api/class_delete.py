# @Time   ：2023/3/3 14:39
# @Author : Chao
# @File   : class_delete.py

import requests
import allure
from requests import Response

@allure.step("删除知识分类")
def class_delete(s, base_url, classes_id, domain_id) ->Response:
    """

    :param s:
    :param base_url:
    :param classes_id: 分类id
    :param domain_id:  知识类型id，知识点：1 文库：2 案例：19 视频：18
    :return:
    """
    url = base_url+"/aikn-admin/knowledge/knowledge/v1/classes?classesId="+ classes_id + "&domainId=" + domain_id
    r = requests.delete(url) #HTTP Delete
    js = r.json() #解析json（如果该接口响应的是content-type是json格式的数据）
    cookie1 = r.cookies #获得cookie数据
    return s.delete(url, json=js, cookies=cookie1)

if __name__ == '__main__':
    base_url="https://v6-stable.faqrobot.com.cn"
    from api.login_function import login
    login(s,base_url)
    result=class_delet(s,base_url)
    print(result.text)