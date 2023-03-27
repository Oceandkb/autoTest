# @Time   ：2023/3/17 13:22
# @Author : Chao
# @File   : test_video_upload.py

import allure
from aikn_api.video_upload import video_upload
import requests

@allure.epic("知识库")
@allure.feature("知识")
@allure.story("视频库")
@allure.title("上传视频成功")
def test_video_upload(login_fixture, base_url):
    r = video_upload(login_fixture, base_url, file_path = '/Users/iyunwen/Desktop/zhishiku-stable/video/Grass.mp4')
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '上传成功.'