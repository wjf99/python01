# ## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
user_list = [{"role": "user", "account": "zhangsan", "password": "123456", "dep": "test"},
             {"role": "admin", "account": "admin", "password": "111111", "dep": "boss"}]
username = input("请输入账号名：")
password = input("请输入密码：")
code=0
def Login():

    if len(username)==0 or len(password) ==0:
        print("请输入正确的用户名或者密码！！！")
    elif len(password)<6:
        print("请输入正确的用户名或者密码！！！")
    elif username  in user_list[0].values() and password  in user_list[0].values():
        login_mess = {'code':0,'message':'登录成功'}
        login_mess.update(user_list[0])
        print(login_mess)
    elif username  in user_list[1].values() and password  in user_list[1].values() :
        login_mess = {'code':0,'message':'登录成功'}
        login_mess.update(user_list[1])
        print(login_mess)
    else:
        login_mess = {'code': 1, 'message': '登录失败'}
        print(login_mess,"登录失败，请检查您的用户名或密码是否填写正确!!!")

def Select():
    pass

Select()
Login()


