# @Time   ：2023/8/15 13:31
# @Author : Chao
# @File   : course_add.py


import allure
import requests
from requests import Response

@allure.step("新增课件")
def courseware_add(s, base_url, is_download, courseware_name, field_id, classes_id, material_data, material_id) -> Response:
    '''

    :param s:
    :param base_url:
    :param is_download:
    :param courseware_name:
    :param field_id:
    :param classes_id:
    :param material_data: courseware_doc_upload请求的返回json
    :param material_id: int型
    :return:
    '''

    url = base_url + "/knside-admin/exam/courseware/v1/add"
    h = {
        "Accept": "application/json, text/plain, */*"
        }
    body = {
        "isDownload": is_download,
        "classesId": classes_id,
        "coursewareName": courseware_name,
        "fieldId": field_id,
        "coursewareMaterialList": [material_data],
        #将courseware_doc_upload（上传课件附件）请求中返回的json数据作为course_add请求入参的一部分，避免定义太多变量去赋值
        "materialIds": [
            material_id
        ],
        "openToField": "," + field_id + ",",
        "examquestionIdList": []
    }

    s.headers.update(h)
    r = s.post(url, json = body)
    print(r.request.body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    from aikn_api.courseware_doc_upload import courseware_doc_upload
    login(s, base_url)
    r1 = courseware_doc_upload(s, base_url, file_path='/Users/iyunwen/Desktop/zhishiku-stable/material/bank.doc')
    r2 = r1.json()['data']
    id = r1.json()['data']['id']
    print(r2)
    print(id)
    result = courseware_add(s, base_url, is_download = 0, courseware_name = 'test_course01', field_id = '251', classes_id = '-1',
                            material_data = r2, material_id = id)
    print(result.text)
