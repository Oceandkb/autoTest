# 项目介绍
这是接口自动化测试

用例报告输出
+ pytest --alluredir ./report/robot --clean-alluredir -m smoke   
+ --筛选并执行命令，标记（smoke）在pytest.ini文件中添加
+ allure serve -p 8800 ./report/robot     
+ --输出报告  



+ for x in r:  
  print(r.text)  
  换行输出list



+ r1 = kn_att_search(login_fixture, base_url)  
  r1_json = r1.json()  
  id = r1_json['data']['list'][1]['id']  
  提取response中列表中的数据，首先将返回的数据转换成为json格式，  
  然后将list中索引位置为1的数据的id赋值给变量id


+ 随机生成整数 random.randint(a,b) [a,b代表上下限]


+ 定义fixture时，scope参数代表的是fixture的应用范围，session>module>class>funtion


+ 使用fixture时 yield后的对象是作为调用fixture时传的参数
+ 当一个fixture中有两个或者多个要传的参数时，可以将参数用元组的方式存储，在调用时使用如下code：

```python
# fixture中
import pytest

@pytest.fixture()
def fixture():
  a = 1
  b = 2
  yield a,b

@pytest.mark.usefixtures("fixture")
# 调用时
def login(fixture):
  login(s, fixture[0]) 
```


## fixture返回None

```python
@pytest.fixture(scope="session")
def my_fixture():
    my_list = []
    if len(my_list) == 0:
    #    pass  #pass，默認返回None
        yield None
    else:
        yield my_list
```
但是在使用这个fixture时，会提示"Fixture 'fixture_name' has no return value"，所以改成yield或者reture None，确保程序不会报错