# @Time   ：2022/11/18 13:24
# @Author : Chao
# @File   : entry_search.py


import allure
import requests
from requests import Response

@allure.step("列表查询词条")
def entry_list_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/knowledge/entry/v1/list-entry"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    body = {
        "pageNum":1,
        "pageSize":10,
        "data":{"entryWords":None,"domainId":1,"question":"","queryRanges":[],"classesIds":[],"questionType":3}
    }
    s.headers.update(h)
    r = s.post(url, json = body)
    #r_json = r.json()
    return r

@allure.step("总览搜索词条")
def entry_elasticsearch(s, base_url, entry_name) -> Response:

    url = base_url + "/aikn-app/knowledge/search/v1/elasticsearch"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    body = {
                "data" : {
                "question": entry_name,
                "domainId": 1,
                "queryRanges": [1,7],
                "searchFieldIds": [],
                "questionType": [3],
                "fileSize": [],
                "dispatchTimeStart": "",
                "dispatchTimeEnd": "",
                "labelIds": [],
                "status": "",
                "effectiveStartTime": "",
                "effectiveEndTime": "",
                "channelIds": [],
                "answerTypes": [],
                "createUserIds": [],
                "knowledgeLabelIds": [],
                "dateLabelIdMapList": [],
                "entryWords": [],
                "classesIds": [],
                "sortType": 0,
                "bertSearch": 0,
                "groupLabelIds": [],
                "excludeLabelIds": [],
                "excludeEntryWords": [],
                "groupEntryWords": [],
                #"debugShow": false,
                "lastQuestionList": []
                }
        }

    s.headers.update(h)
    r = s.post(url, json = body)
    #r_json = r.json()
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = entry_elasticsearch(s, base_url, "2222")
    print(result.text)