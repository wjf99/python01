# ## 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。
#
user_list = [{"role": "user", "account": "zhangsan", "password": "123456", "dep": "test"},
             {"role": "admin", "account": "admin", "password": "111111", "dep": "boss"}]
username = input("请输入账号名：")
password = input("请输入密码：")
flag=0
def Login():

    if len(username)==0 or len(password) ==0:
        print("请输入正确的用户名或者密码！！！")
    elif len(password)<6:
        print("请输入正确的用户名或者密码！！！")
    elif username  in user_list[0].values() and password  in user_list[0].values():
        login_mess = {'message':'登录成功'}
        login_mess["code"]=0
        login_mess.update(user_list[0])
        print(login_mess)
        flag=0
    elif username  in user_list[1].values() and password  in user_list[1].values() :
        login_mess = {'message': '登录成功'}
        login_mess["code"] = 0
        login_mess.update(user_list[1])
        print(login_mess)
        flag = 0
    else:
        login_mess = {'message': '登录成功'}
        login_mess["code"] = 1
        print(login_mess,"登录失败，请检查您的用户名或密码是否填写正确!!!")
        flag = 1

def Select():
    if flag==0:
        pass
    else:
        print("请先登录！！！")

Select()
Login()