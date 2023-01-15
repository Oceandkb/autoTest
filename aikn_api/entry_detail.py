# @Time   ：2022/12/2 14:24
# @Author : Chao
# @File   : entry_detail.py
import allure
import requests
from requests import Response
"/aikn-app/knowledge/knowledge/v1/knowledge-detail/1128567?flag=1&isAttribute=1&isCheck=0"

@allure.step("查看词条详情")
def entry_detail(s, base_url, entry_id) ->Response:
    url= base_url + "/aikn-app/knowledge/knowledge/v1/knowledge-detail/" + entry_id +"?flag=1&isAttribute=1&isCheck=0"
    r=requests.get(url)
    js=r.json() # 解析json（如果该接口响应的是content-type是json格式的数据）
    cookie1=r.cookies# 获得cookie数据
    res=s.get(url, json=js, cookies=cookie1)
    return res

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = entry_detail(s, base_url, entry_id = "1128567")
    print(result.text)