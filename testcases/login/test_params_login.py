'''
import allure
import pytest, requests
from api.login_function import login
from utils.read_yml import readyml
from pathlib import Path
p = Path(__file__)
yamlPath = p.parent.parent.parent.joinpath('data', 'data.yaml')
test_data = readyml(yamlPath)['login']


@allure.title("参数化测试")
@pytest.mark.login
@pytest.mark.parametrize("test_input, expected",
                         test_data
                         )
def test_login_params(base_url, test_input, expected):
    print("测试数据:", test_input)
    s = requests.Session()
    r = login(s,  base_url, **test_input)
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]
'''