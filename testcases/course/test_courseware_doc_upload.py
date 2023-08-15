# @Time   ：2023/8/15 14:17
# @Author : Chao
# @File   : test_courseware_doc_upload.py


import allure
from aikn_api.courseware_doc_upload import courseware_doc_upload
import requests

@allure.epic("知识库")
@allure.feature("学院")
@allure.story("课程")
@allure.title("上传课件附件成功")
def test_courseware_doc_upload(login_fixture, base_url):
    r = courseware_doc_upload(login_fixture, base_url,
                              file_path = '/Users/iyunwen/Desktop/zhishiku-stable/material/bank.doc')
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '上传成功.'