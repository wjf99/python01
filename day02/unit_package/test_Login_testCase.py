# 存在的问题

'''
1、无法查看运行的用例数，比如成功了几条，失败了几条
2、如果失败了，是什么原因导致的？最好给出失败的错误日志
3、无法阻止用例，不能控制那些用例执行，那些不执行
'''

# 解决方案： 使用unitTest去解决


'''1、将不同的测试用例添加到不同套件中
2、将不同的测试套件进行运行
3、能对各测试用例进行测试（断言），也能看到测试结果
4、可以进行批量添加测试用例'''
# 什么是unitTest
# 包含以下四个类

'''
a、TestCase()功能:
1、可以进行断言
2、测试可查看结果，可以查看失败的原因
3、可以进行初始化和消除功能


b、TestSuite()功能
1、可以添加不同的测试用例到套件中（单条）
2、可以添加不同的测试用例组到套件中（一组）

c、 TextTestRunner()功能
可以将测试套件进行运行

d、TestLoader()
 可以进行批量运行测试用例
'''
'''
a、TestCase()功能:
1、可以进行断言
2、测试可查看结果，可以查看失败的原因
3、可以进行初始化和消除功能


'''
from day01.demo_userAdd import Delu, get_data_from_file
import unittest
import sys
user_list=[]
user_list=user_list if user_list else get_data_from_file("user_data")
class Login_Test(unittest.TestCase):

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("此处的类方法是：",sys._getframe().f_code.co_name)

    @classmethod
    def tearDownClass(cls) -> None:
        print("此处的类方法是：", sys._getframe().f_code.co_name)
    # 初始化清除方法
    # 初始化方法
    def setUp(self) -> None:
        print("此处的方法是：",sys._getframe().f_code.co_name)
    # 清除方法
    def tearDown(self) -> None:
        print("此处的方法是：",sys._getframe().f_code.co_name)

# 测试登录的测试用例
# case1 :输入正确的用户名和密码
    def test_login_success(self):
        print("此处的方法是：", sys._getframe().f_code.co_name)
        except_value=0
        actul_value=Delu("admin","111111").get("code")
        self.assertEqual(except_value,actul_value)

# case2: 输入错误的用户名
    def test_login_error(self):
        print("此处的方法是：", sys._getframe().f_code.co_name)
        except_value=1
        actul_value=Delu("aaaaa","111111").get("code")
        self.assertEqual(except_value,actul_value)

# case3: 输入空的密码
    def test_login_null(self):
        print("此处的方法是：", sys._getframe().f_code.co_name)
        except_value=1
        actul_value=Delu("","").get("code")
        self.assertEqual(except_value,actul_value)

if __name__ == '__main__':
    unittest.main()

