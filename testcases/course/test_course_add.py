# @Time   ：2023/8/18 14:29
# @Author : Chao
# @File   : test_course_add.py


import pytest
import allure
from aikn_api.field_search import field_search
from aikn_api.class_search import class_search
from aikn_api.material_search import material_search
from aikn_api.course_add import course_add

@allure.epic("知识库")
@allure.feature("学院")
@allure.story("课程")
@allure.title("新增课程成功")
@pytest.mark.usefixtures("courseware_search_fixture")
@pytest.mark.parametrize('material_search_fixture', ['1'], indirect=True)
def test_course_add(login_fixture, base_url, field_search_fixture, courseware_search_fixture,
                 datetime_fixture, material_search_fixture):
    r = course_add(login_fixture, base_url, field_id=field_search_fixture,course_name = datetime_fixture + "课程",
                   class_id = '-1',cover_path=material_search_fixture, serial_name="Chapter 1", content_type=4,
                   content_id=courseware_search_fixture[0], content_name=courseware_search_fixture[1])
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'