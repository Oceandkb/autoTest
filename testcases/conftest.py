from aikn_api.login_function import login
from aikn_api.wiki_class_add import wiki_class_add
from aikn_api.kn_att_add import *
from aikn_api.kn_att_search import *
from aikn_api.entry_add import entry_add
from aikn_api.entry_search import *
from aikn_api.entry_delete import entry_delete
import pytest
import requests
import random


@pytest.fixture(scope="session")
def login_fixture(base_url):
    """全局登录 session会话"""
    s = requests.Session()
    login(s, base_url)
    yield s
    s.close()

@pytest.fixture(scope="session")
def wiki_class_add_fixture(login_fixture, base_url):
    wc = wiki_class_add(login_fixture, base_url)
    return wc

@pytest.fixture(scope="session")
def random_fixture():
   """

   :rtype: 随机汉字名称
   """
   ran = random.randint(0x4e00, 0x9fbf)
   name = chr(ran) + "分类"
   yield name

@pytest.fixture(scope="session")
def kn_att_fixture(login_fixture, base_url, random_fixture):
    kn_text_att_add(login_fixture, base_url, random_fixture)
    r_att_search = kn_all_att_search(login_fixture, base_url)
    r_json = r_att_search.json()
    att_id = str(r_json['data']['list'][0]['id'])
    print(att_id)
    yield att_id


@pytest.fixture(scope="session")
def entry_fixture(login_fixture, base_url, random_fixture):
    '''查询词条setup：新增词条，列表查询新增的词条名称'''
    entry_add(login_fixture, base_url, random_fixture)
    r = entry_list_search(login_fixture, base_url)
    r_json = r.json()
    entry_name = r_json['data']['list'][0]['questions'][0]['question']
    entry_id = str(r_json['data']['list'][0]['id'])
    entry_question_id = str(r_json['data']['list'][0]['questions'][0]['id'])
    print(entry_name,entry_id,entry_question_id)
    yield entry_name, entry_id, entry_question_id
    d = entry_delete(login_fixture, base_url, entry_id)
    print(d.text)


