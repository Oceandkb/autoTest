# @Time   ：2023/8/15 14:21
# @Author : Chao
# @File   : test_courseware_add.py


import allure
import pytest
from aikn_api.courseware_add import courseware_add
from aikn_api.courseware_doc_upload import courseware_doc_upload
from aikn_api.field_search import field_search
import requests

@allure.epic("知识库")
@allure.feature("学院")
@allure.story("课程")
@allure.title("添加课件成功")
@pytest.mark.usefixtures("course_material_fixture")
def test_courseware_add(login_fixture, base_url, course_material_fixture, random_fixture):
    #r0 = field_search(login_fixture, base_url)
    #field_id = r0.json()['data']['id']
    #print(field_id)
    r = courseware_add(login_fixture, base_url, is_download = 0, courseware_name = random_fixture('课程'),
                              field_id = '251', classes_id = '-1',
                              material_data = course_material_fixture[0], material_id = course_material_fixture[1])
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'