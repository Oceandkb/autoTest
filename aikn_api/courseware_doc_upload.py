# @Time   ：2023/8/15 11:15
# @Author : Chao
# @File   : upload_to_pdf.py

import allure
import requests
from requests import Response

@allure.step("上传课件附件")
def courseware_doc_upload(s, base_url, file_path) -> Response:

    url = base_url + "/admin/public/file/v1/material/course/upload_to_pdf"
    h = {
        "Accept": "*/*",
        'Content-Length': '4794424',
    }
    data = {
           "file": open(file_path, 'rb')  #该接口的content-type为multipart/form-data
    }
    s.headers.update(h)
    r = s.post(url, files = data)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = courseware_doc_upload(s, base_url, file_path='/Users/iyunwen/Desktop/zhishiku-stable/material/bank.doc')
    print(result.text)