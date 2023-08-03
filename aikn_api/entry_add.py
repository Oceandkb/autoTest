# @Time   ：2022/11/18 13:57
# @Author : Chao
# @File   : entry_add.py


import allure
import requests
from requests import Response
import random

@allure.step("新增词条")
def entry_add(s, base_url, entry_name, field_id) ->Response:
    url = base_url + "/aikn-admin/knowledge/entry/v1/add-entry/"
    ran = str(random.randint(1, 1000))
    #entry_name = "auto_entry" + ran
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "classIds": [-1],
        "question": {"question": entry_name, "id": ""},
        "readPermissions": [],
        "currentField": field_id,
        "field": [field_id],
        "buildRelationText": "",
        "knowledgeType": None,
        "knowledge": {
            "id": "",
            "openToCustomer": 1,
            "description": "",
            "removeDuplicate": 1
        },
        "knowledgeFieldLabelList": [],
        "knowledgeClassesLabelList": [],
        # "entryAnswers": [
        #     {
        #         "hierarchy": 0,
        #         "name": "知识对比，默认领域1，2个词条【适用单位】",
        #         "relateKnowledgeId": 982449,
        #         "serialNumber": "4.",
        #         "type": 2,
        #         "answer": "<p>2022年3月3日17:16:15</p>",
        #         "id": 982449,
        #         "fieldId": 161,
        #         "fieldName": "默认领域",
        #         "status": "启用",
        #         "effectTime": "永久",
        #         "capacitySize": 30,
        #         "visible": 1,
        #         "hierarchyName": "一级"
        #     }
        # ],
        "summary": "",
        "draftId": "",
        "requirementId": 0,
        "entryAttributeIds": [],
        "videoRelation": []
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url, user = "autoSite", password = "123456Abc!")
    result = entry_add(s, base_url, entry_name = "test11", field_id=197)
    print(result.text)