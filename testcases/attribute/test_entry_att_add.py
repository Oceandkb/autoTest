import allure
import requests
from aikn_api.entry_att_add import entry_att_add


@allure.epic("知识库")
@allure.feature("属性")
@allure.story("词条属性")
@allure.title('新增词条属性成功')
# @pytest.mark.smoke
def test_entry_att_add(login_fixture, base_url):
    r = entry_att_add(login_fixture, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'


