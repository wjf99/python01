# 测试用例过多，导致代码冗余，维护性不高，主要原因：就是代码重读，数据不同

#解决方法：使用parameterized 实现数据参数化，将列表中的数据在一条测试用例中循环执行，起到多条测试的作用


# 具体方法： expand(list),list:数据列表
#备注：使用expand(),需要把它放在测试方法前，加@，这个叫装饰器
# 前置条件  pip install parameterized

# 1、导包

from parameterized import parameterized
import unittest
# 测试数据
from day01.demo_userAdd import Delu

list_data=[(0,'admin',"111111"),(1,"abc","123456")]

class TestLogin(unittest.TestCase):
    @parameterized.expand(list_data)
    def test_login(self,except_value,username,password):
        actul_value=Delu(username,password).get("code")
        self.assertEqual(except_value,actul_value)
if __name__ == '__main__':
    unittest.main()
