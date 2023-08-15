# @Time   ：2023/8/15 15:11
# @Author : Chao
# @File   : pdf_convert.py

import allure
import requests
from requests import Response

@allure.step("上传文件转换pdf")
def pdf_convert(s, base_url, material_id) -> Response:

    url = base_url + "aikn-admin/api/file/v1/file-convert/pdf/" + material_id
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    return

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    from aikn_api.courseware_doc_upload import courseware_doc_upload
    login(s, base_url)
    r1 = courseware_doc_upload(s, base_url, file_path='/Users/iyunwen/Desktop/zhishiku-stable/material/bank.doc')
    id = str(r1.json()['data']['id'])
    result = pdf_convert(s, base_url, material_id = id)
    print(result.text)
