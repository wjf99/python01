from loguru import logger
# 1、测试登录的测试用例（单元测试）
# case1 : 输入正确的用户名和正确的密码进行登录
# case2 : 输入错误的用户名和正确的密码进行登录
# case3: 输入空的用户名和正确的密码进行登录

#2、进行测试 - 使用断言 assert 值1 操作符  值2
# 测试方式：预期结果和实际结果 进行比较

# 以上用例 登录成功的预期结果是code=0
from day01.Delu import Delu

result =Delu("admin","111111")
logger.debug("登录返回数据{}".format(result))
assert 0==result.get("code")
assert 1==result.get("code")
# 2022-06-01 16:32:43.525 | DEBUG    | __main__:<module>:14 - 登录返回数据{'code': 0, 'message': '登录成功！', 'user_List': {'role': 'admin', 'account': 'admin', 'password': '111111', 'dep': 'boss'}}

# 存在的问题

'''
1、无法查看运行的用例数，比如成功了几条，失败了几条
2、如果失败了，是什么原因导致的？最好给出失败的错误日志
3、无法阻止用例，不能控制那些用例执行，那些不执行
'''