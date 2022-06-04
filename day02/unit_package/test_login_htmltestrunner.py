# 问题： 用unittest的测试报告太简单，只能在控制台查看，想生成的测试报告更详细，能在浏览器中打开

#解决方案：使用HTMLTestRunner模块生成测试报告，原理：将运行的测试用例结果输出到了HTML文件中，就能在浏览器打开

#前置条件 直接现成的

from day02.unit_package.HTMLTestRunner import HTMLTestRunner

from day01.demo_userAdd import Delu, get_data_from_file
import unittest
import sys
user_list=[]
user_list=user_list if user_list else get_data_from_file("user_data")
class Login_Test(unittest.TestCase):



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
'''
类： HTMLTestRunner(f,title,description)
    f :是指文件对象，一般是HTML文件
    title:生成的测试报告标题
    description:生成测试报告的描述
'''
if __name__ == '__main__':
    # 创建一个条件 a
    suite_a=unittest.TestSuite()
    suite_a.addTest(Login_Test("test_login_success"))
    suite_a.addTest(Login_Test("test_login_error"))
    suite_a.addTest(Login_Test("test_login_null"))

    # 创建一个测试报告文件，HTML格式
    test_report='./test_report.html'
    with open(test_report,"wb") as f:
        runner = HTMLTestRunner(f, title="测试报告", description="测试报告描述")
        runner.run(suite_a)

