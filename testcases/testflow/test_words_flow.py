'''
#登录-1.添加word-2.查询word-3.修改word-4.删除word

from api.professional_words_function import add_words, update_words, get_words, detele_words
import pytest
import datetime


#@pytest.mark.smoke
def test_words_workflow(login_fixture, base_url):
    """流程性的用例"""
    # step-1
    word_name = "专业名词" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    new_word_name = "修改的名词" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    r1 = add_words(login_fixture, base_url, word_name)
    print(r1.text)
    # step-2
    r2 = get_words(login_fixture, base_url)
    print(r2.json()["data"]["list"][0])
    print(r2.json()["data"]["list"][0]["id"])
    word_id = r2.json()["data"]["list"][0]["id"]
    print(r2.text)
    # step-3
    r3 = update_words(login_fixture, base_url, new_word_name, word_id)
    print(r3.text)
    # step-4
    r4 = detele_words(login_fixture, base_url, word_id)
    print(r4.text)

'''