# Time：2022/10/11 14:36
# Author: chao
import requests

url="https://v5-test.faqrobot.cn/aikn-admin/knowledge/knowledge/v1/classes?classesId=62545&domainId=1"
r=requests.delete(url)
print(r.status_code)
