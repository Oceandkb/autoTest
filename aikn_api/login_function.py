import jpype
import requests
from requests import Response
import configparser
from pathlib import Path
import os

p = Path(__file__)
user_info_path = p.parent.parent.joinpath("pytest.ini")
config = configparser.ConfigParser()
config.read(user_info_path, encoding="utf-8")

username = config["pytest"]["username"]
password = config["pytest"]["password"]

print("读取的账户信息：" + config["pytest"]["username"])
print("读取的密码信息：" + config["pytest"]["password"])


def login(s, base_url, user = username, password = password) -> Response:
    a = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(a, "encryption.jar")
#---------------------------------------------------------------------------------------------------------------+
    url1 = base_url + "/base-admin/public/sso/v1/login/keyPair"

    r = s.post(url1)  # 调用post方法来发送请求，获取响应
    str1 = r.json()["data"]["Modulus"]    #将请求url1获取的json相应内容存储到str1中（字符串格式）
    str2 = r.json()["data"]["Exponent"]
    print(str1)
    jvm_path = jpype.getDefaultJVMPath() #
    if not jpype.isJVMStarted():  # 判断jvm是否启动
        jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=%s" % data_path)   # 若没有启动，启动jvm

    encry_class = jpype.JClass("com.iyunwen.crypto.Encrypto")
    enctypt_pwd = encry_class().encrypt(str1, str2, password)
#------------------------------------------------------------------------------------------------------------

    url = base_url + "/base-admin/login"
    h = {
        "Accept": "application/json, text/plain, */*"    #请求头信息记录在变量h中
    }
    s.headers.update(h)   #更新请求头信息
    body = {
        "username": user,
        "password": str(enctypt_pwd),
        "isRememberMe": False
    }
    r = s.post(url, data=body)
    return r

if __name__ == '__main__':    # 在python中相当于主函数的入口（类似于java中的main函数）
    s1 = requests.session()  # 创建session对象，用于发送请求，session可以记录cookie信息，不需要每次都把cookie都放到请求参数中
    r2 = login(s1, base_url="https://v6-stable.faqrobot.com.cn")
    print("r2.text结果是：", r2.text)
