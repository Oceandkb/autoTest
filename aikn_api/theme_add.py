# @Time   ：2023/7/11 21:43
# @Author : Chao
# @File   : theme_add.py



# @Time   ：2023/3/3 9:34
# @Author : Chao
# @File   : api_demo.py


import allure
import requests
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("新增主题")
def theme_add(s, base_url, theme_name, cover, poster) -> Response:

    url = base_url + "/aikn-admin/theme/management/v1/theme/save"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    #kn_text_att_name = "Auto" + ran
    body = {
        "themeBaseInfo":
            {
                "id": "",
                "name": theme_name,
                "titleFontColour": "#FFFFFF",
                "titleFontSize": 26,
                "description": "",
                "descFontSize": 14,
                "descFontColour": "#FFFFFF",
                "scope": 1,
                "coverType": 2,
                "coverPic": cover,
                "posterType": 2,
                "posterPic": poster,
                "type": 1,
                "style": 1
            },
        "secondaryThemeConfigList":
            [{
                "themeLayoutConfDTOList": []
            }]
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url, user = "aiknSite", password = "123456Abc!" )
    values = [1, 2, 4, 5, 6, 7, 8, 9]
    for n in range(1,11):
            result = theme_add(s, base_url, theme_name = n, cover = 6, poster = 1)
    print(result.text)



