# @Time   ：2023/3/17 11:15
# @Author : Chao
# @File   : video_upload.py

import os
import allure
import requests
import random
import tkinter as tk
from tkinter import filedialog
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("上传视频")
def video_upload(s, base_url, file_path) -> Response:
    """

    :param s:
    :param base_url:
    :param file_path: 本地文件的路径
    :return:
    """
    url = base_url + "/aikn-admin/video-library/management/v1/video-upload"
    h = {
        "Accept": "*/*",
        'Content-Length': '300000',
    }
    # file_path = video_path       #'/Users/iyunwen/Desktop/video/mp4/wood.mp4'
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
    result = video_upload(s, base_url)
    print(result.text)