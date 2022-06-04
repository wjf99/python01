import unittest

from day01.Delu import Delu


class TestLogin(unittest.TestCase):
# 测试登录的测试用例
# case1 :输入正确的用户名和密码
    def test_login_success(self):
        except_code=0
        actual_code=Delu("admin","111111").get("code")
        self.assertEqual(except_code,actual_code)
# case2: 输入错误的用户名
    def test_login_error(self):
        except_code=1
        actual_code=Delu("abc","111111").get("code")
        self.assertEqual(except_code,actual_code)
# case3: 输入空的密码
    def test_login_null(self):
        except_code=1
        actual_code=Delu("admin","").get("code")
        self.assertEqual(except_code,actual_code)

if __name__ == '__main__':
    unittest.main()


