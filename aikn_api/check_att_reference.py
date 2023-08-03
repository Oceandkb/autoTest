# @Time   ：2023/8/3 15:46
# @Author : Chao
# @File   : check_att_reference.py



import allure
import requests
from requests import Response


@allure.step("检查属性是否有被引用")
def check_att_reference(s, base_url, att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label/field?labelId=" + att_id
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = check_att_reference(s, base_url, "551")
    print(result.text)


