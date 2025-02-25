今日课题:Pytest自动化测试框架从入门到大成实战训练营  
金牌讲师:码尚教育-百里老师  
直播时间:20:00-22:00  
1. 单元测试框架分类以及作用  
2. pytest简介以及常用插件安装  
3. pytest默认测试用例规则和基础应用
4. pytest运行方式以及常用参数详解
5. pytest测试用例的执行顺序
6. pytest测试用例markers分组执行
7. pytest跳过测试用例装饰器
8. pytest测试用例的前后置，固件，夹具  
上课地址:https://ke.qq.com/course/3061635?taid=10551149806401411


## 一、单元测试框架
1. 什么是单元测试框架  
单元测试框架是在自动化测试或者白盒测试中对软件的最小单元(函数，方法)进行测试的框架
2. 单元测试框架分类  
Python:unittest,pytest( 主流)
Java:Testng(主流)和Junit
3. 单元测试框架主要做什么?
发现测试用例
执行测试用例
判断测试结果
生成测试报告


## 二、Pytest简介以及常用插件安装
1. pytest是一个非常成熟的单元测试框架。灵活和简单
2. 它可以结台selenium，requests，appium完成各种不同的自动化
3. 它还可以生成自定义allure报告以及和Jenkins持续集成
4. pytest有很多强大的插件。  
      pytest  
      pytest-html(生成htm报告的插件)  
      pytest-xdist(多线程运行的插件)  
      pytest-ordering(改变用例的执行顺序的插件)  
      pytest-rerunfaiires(失败用例重跑的插件)  
      allure-pytest(生成美观自定义的allure报告)

通过在项目的根目录下新建一个:requirements.txt文件保存插件。然后使用以下命令安装:  
```pip install -r requirements.txt```



## 三、pytest默认测试用例的规则以及基础应用
1. 模块名必须以 test_ 开头或者 _test 结尾。
2. 测试类必须以Test开头，并且不能带有init方法。
3. 测试用例必须以 test_ 开头。



**执行:Alt+Enter自动导包**

1. 通过命令行方式执行  
```pytest``` 

**执行的参数:**   
-vs   -v:输出详细信息。  -s:输出调试信息。如:  
```pytest -vs ```  
-n    多线程运行(前提安装插件:pytest-xdist)。如:  
```pytest -vs -n=2 ```  
--reruns num   失败重跑(前提安装插件:pytest-rerunfailres)。如:  
```pytest -vs --reruns=2 ```   
      **raise Exception()       抛出异常**  
      **try except              解决异常**  
-x    出现一个用例失败则停止测试。如:  
```pytest-vs -x ```   
--maxfail   出现几个失败才终止。如:  
```pytest -vs --maxfail=2 ```  
--html      生成html的测试报告(前提安装插件:pytest-html)。如:  
```pytest -vs --html ./reports/result.html ```  
-k    运行测试用例名称中包含某个字符串的测试用例。如:  
```pytest -vs -k "baili or yiran" ```



2. 通过主函数main方式执行。  
```
if __name__=='__main__':  
      pytest.main(["vs"]) 
```

3. 通过全局配置文件pytest.ini文件执行。  
**注意:**  
一般放在项目的根目录下，名称必须是pytest.ini    
当有中文时可能需要改变编码格式为GB2312     
pytest.ini文件可以改变默认的测试用例规则。    
不管是命令行运行也好还是说主函数运行也好，都会加载这个配置文件。  
```
[pytest]    

# 默认规则: 参数
# addopts = -vs 
addopts = -vs -m "smoke"   # 装饰器
testpaths = ./testcases
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# 测试用例分组执行 
markers =
      smoke:冒烟用例
      mashang:码尚教育
      product manage:商品管理模块用例
      user manage:用户管理模块
      
```
这里 -m "smoke"表示只执行冒烟用例  



## 四、pytest跳过测试用例。

(1)无条件跳过  
`@pytest.mark.skip(reason="无理由跳过”)`  
(2)有条件跳过  
`@pytest.mark.skipif(workage<10,reason="工作经验少于10年跳过”`


## 五、pytest测试用例的前后置，固件
**common_util.py**
```
class CommonUtil:

      # 前四个方法是类方法，用做前后置处理

      def setup_class(self):
          print("每个类之前执行一次")


      def teardown_class(self):
          print("每个类之后执行一次")


      def setup_method(self):
          print("每个用例之前执行一次")


      def teardown_method(self):
          print("每个用例之后执行一次")

```
 





