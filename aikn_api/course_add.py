# @Time   ：2023/8/16 15:59
# @Author : Chao
# @File   : course_add.py

import allure
import requests
from requests import Response

@allure.step("新建课程")
def course_add(s, base_url, field_id, course_name, class_id, cover_path, serial_name,
               content_type, content_id, content_name) -> Response:
    '''

    :param s:
    :param base_url:
    :param field_id: 课程领域，str
    :param course_name: 课程名称，str
    :param class_id: 课程分类，str
    :param cover_path: 课程封面路径，str
    :param serial_name: 课程章节名称， str
    :param content_type: 章节中的学习内容类型，课件4，知识点2, 文库3
    :param content_id: 学习内容id，从查询接口获取， int
    :param content_name: 学习内容名称，从查询接口获取，str
    :return:
    '''

    url = base_url + "/knside-admin/exam/course/v1/add"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "isDownload": 0,
        "openToField": "," + str(field_id) + ",",
        "fieldIds": [
            field_id
        ],
        "courseName": course_name,
        "classesId": class_id,
        "coverMaterial": cover_path,
        "userIds": [],
        "materialIds": [],
        "courseDetails": [
            {
                "type": 1,
                "serialNumber": "第一章",
                "name": serial_name,
                "learnContentList": [
                    {
                        "type": content_type,
                        "contentId": content_id,
                        "name": content_name,
                        "serialNumber": "1.1"
                    }
                ]
            }
        ],
        "examquestionIdList": [],
        "isShow": 0,
        "isCheck": 0,
        "ifPush": 0,
        "ifExtract": 0
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = course_add(s, base_url, field_id=251, course_name="test0001", class_id='-1',
                        cover_path='/upload/public/material/101/20230811/DD6F4ABC76A841F08E2843A3517039BE.png',
                        serial_name='0001', content_type=4,content_id=23,content_name='2023-08-16_17-16-41课件')
    print(result.text)
