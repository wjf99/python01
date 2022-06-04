
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

# 1、使用TestLoader()，可以批量去添加测试用例（作用），解决单条用例效率问题

'''
d、 TestLoader():
   1、可以进行批量运行测试用例： discover(test_dir,patten='test*.py')
     test_dir :要搜索的路径
     patten  : 指定匹配的模式，在test_dir目录下搜索所有的patten文件
'''
if __name__ == '__main__':
    # 创建一个条件 a
    suite_a=unittest.TestLoader().discover(".",pattern='test_login*.py')
    #print(suite_a)
    runner=unittest.TextTestRunner()
    runner.run(suite_a)