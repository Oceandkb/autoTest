# @Time   ：2023/3/16 9:48
# @Author : Chao
# @File   : case_add.py

import allure
import requests
import random
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("新增案例")
def case_add(s, base_url, case_name, rich_text_content, edit_type, class_id, field_id, open_field_id, markdown_content) \
        -> Response:
    """

    :param s:
    :param base_url:
    :param case_name: 案例名称, str
    :param rich_text_content: 富文本框编辑内容，传入rich_text_content时，edit_type需为2；str，选择一种编辑模式，
                              另一个编辑模式的content参数不传
    :param edit_type: 编辑模式，值包括2（富文本框编辑模式）和1（markdown编辑模式）, int
    :param class_id: 案例的分类id，str
    :param field_id: 案例的领域id，str
    :param open_field_id: 案例开放领域的id，str
    :param markdown_content: markdown编辑内容，传入markdown_content时，edit_type需为1； str
    :return:
    """
    url = base_url + "/aikn-admin/knowledge/case/v1/case"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "markdownContent":"",
        "question":
            {
                "question":case_name,
                "id":""
            },
        "answer":
            {
                "answer":rich_text_content + markdown_content,
                "type":edit_type
            },
        "editType":edit_type,
        "classIds":[class_id],
        "field":[field_id],
        "draftId":"",
        "knowledge":
            {"id":"",
             "openToField":open_field_id
             },
        "markdownContent": markdown_content,
        "materialIds":[],
        "materials":[],
        "ifNewVersion": "true"
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = case_add(s, base_url, case_name = "自动化案例", rich_text_content = "接口测试", edit_type = "2",
                      class_id = "-1", field_id = "261", open_field_id = "261", markdown_content = "")
    print(result.text)

