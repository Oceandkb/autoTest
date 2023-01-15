# @Time   ：2022/12/2 15:35
# @Author : Chao
# @File   : entry_modify.py


import allure
import requests
from requests import Response
import random

@allure.step("修改词条")
def entry_modify(s, base_url, entry_name, entry_id, entry_question_id) ->Response:
    url = base_url + "/aikn-admin/knowledge/entry/v1/add-entry/"
    ran = str(random.randint(1, 1000))
    #entry_name = "auto_entry" + ran
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
            "classIds": [-1],
            "question": {
                "question": entry_name,
                "id": entry_id
            },
            "readPermissions": [],
            "currentField": 261,
            "field": [261],
            "buildRelationText": "",
            "knowledgeType": None,
            "knowledge": {
                "id": entry_question_id,
                "openToCustomer": 1,
                "description": "",
                "removeDuplicate": 1
            },
            "knowledgeFieldLabelList": [],
            "knowledgeClassesLabelList": [],
            "entryAnswers": [],
            "summary": "",
            "draftId": "",
            "requirementId": 0,
            "entryAttributeIds": ["61"],
            "videoRelation": []
        }
    s.headers.update(h)
    r = s.post(url, json = body)
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    entry_modify(s, base_url)
    result = entry_modify(s, base_url)
    print(result.text)