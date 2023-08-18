from aikn_api.login_function import login
from aikn_api.class_add import class_add
from aikn_api.class_search import class_search
from aikn_api.kn_att_add import *
from aikn_api.kn_att_search import *
from aikn_api.entry_add import entry_add
from aikn_api.entry_search import *
from aikn_api.entry_delete import entry_delete
from aikn_api.field_search import field_search
from aikn_api.courseware_doc_upload import courseware_doc_upload
from aikn_api.courseware_search import courseware_search
from aikn_api.material_search import material_search
import pytest
import requests
import random
import datetime

@pytest.fixture(scope="session")
def login_fixture(base_url):
    """全局登录 session会话"""
    s = requests.Session()
    login(s, base_url)
    yield s
    s.close()

@pytest.fixture(scope="session")
def field_search_fixture(login_fixture, base_url):
    '''
    查询默认领域id
    :param login_fixture:
    :param base_url:
    :return:
    '''
    r = field_search(login_fixture, base_url)
    field_id = r.json()['data'][0]['id']
    print(field_id)
    yield field_id

@pytest.fixture(scope="session")
def classId_search_fixture(login_fixture, base_url, request):
    '''
    查询不同知识的默认分类id
    :param login_fixture:
    :param base_url:
    :return:
    '''
    domain_id = request.param
    r = class_search(login_fixture, base_url, domain_id)
    class_id = r.json()['data'][0]['id']
    print(class_id)
    yield class_id

@pytest.fixture(scope="session")
def datetime_fixture():
    # 获取当前日期和时间
    current_time = datetime.datetime.now()

    # 格式化日期和时间为字符串
    formatted_datetime = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    name = f"{formatted_datetime}"
    yield name
def test(datetime_fixture):
    print(datetime_fixture)

@pytest.fixture(scope="session")
def wiki_class_add_fixture(login_fixture, base_url):
    wc = class_add(login_fixture, base_url, domain_id = 1)
    return wc

@pytest.fixture(scope="session")
def random_fixture():
   """
   :rtype: 随机汉字名称
   """
   def _random(name):
     first = random.randint(0xB0, 0xF7)
     last = random.randint(0xA1, 0xFE)
     s = f'{first:x}{last:x}'
     ran = bytes.fromhex(s).decode('gb2312') + name
     return ran
   yield _random

@pytest.fixture(scope="session")
def kn_att_fixture(login_fixture, base_url, random_fixture):
    kn_text_att_add(login_fixture, base_url, random_fixture("文本"))
    r_att_search = kn_all_att_search(login_fixture, base_url)
    r_json = r_att_search.json()
    att_id = str(r_json['data']['list'][0]['id'])
    print(att_id)
    yield att_id


@pytest.fixture(scope="session")
def entry_fixture(login_fixture, base_url, random_fixture):
    '''查询词条setup：新增词条，列表查询新增的词条名称'''
    _r_ = field_search(login_fixture, base_url)
    field_id = str(_r_.json()['data'][0]['id'])
    entry_add(login_fixture, base_url, random_fixture("词条"), field_id)
    r = entry_list_search(login_fixture, base_url)
    entry_name = r.json()['data']['list'][0]['questions'][0]['question']
    entry_id = str(r.json()['data']['list'][0]['id'])
    entry_question_id = str(r.json()['data']['list'][0]['questions'][0]['id'])
    print(entry_name,entry_id,entry_question_id)
    yield entry_name, entry_id, entry_question_id
    # fixture执行结束之后，对产生的数据进行删除
    d = entry_delete(login_fixture, base_url, entry_id)
    print(d.text)

@pytest.fixture(scope="session")
def courseware_upload_material_fixture(login_fixture, base_url):
    '''

    :param login_fixture:
    :param base_url:
    :param file_path: 上传课件素材存储路径
    :return:
    '''
    r = courseware_doc_upload(login_fixture, base_url, 
                              file_path='/Users/iyunwen/Desktop/zhishiku-stable/material/bank.doc')
    _r_ = r.json()['data']
    material_id = r.json()['data']['id']
    print(_r_)
    yield _r_, material_id

@pytest.fixture(scope="session")
def courseware_search_fixture(login_fixture, base_url, field_search_fixture):
    r = courseware_search(login_fixture, base_url, field_search_fixture)
    courseware_id = r.json()['data']['list'][0]['id']
    courseware_name = r.json()['data']['list'][0]['coursewareName']
    print(courseware_id, courseware_name)
    yield courseware_id, courseware_name

@pytest.fixture(scope="session")
def material_search_fixture(login_fixture, base_url, request):
    material_type = request.param
    r = material_search(login_fixture, base_url, material_type)
    path = r.json()['data']['list'][0]['path']
    print(path)
    yield path
