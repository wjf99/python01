# 定义一个方法从文件中取数据
from datetime import datetime


def get_data_from_file(filename):
    try:
        f=None
        f=open(filename,"r")
        line=f.readline()
        user_data=eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

# 定义一个方法向文件中增加数据
# 参数：目标文件，目标数据
def add_data_from_file(filename,filedata):
    try:
        f=None
        f=open(filename,"w")
        f.write(str(filedata))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()





# 定义存储数据的数组
# user_list = [{"role": "user", "account": "zhangsan", "password": "123456", "dep": "test"},
#                  {"role": "admin", "account": "admin", "password": "111111", "dep": "boss"}]
user_list=[]
# 查询数据时，先看列表中有没有，有的话，直接从列表取出，没有的话在文件读取
user_list=user_list if user_list else get_data_from_file("user_data")
user_mess={"code":"","message":""}
#登录
def Delu(username,password):

# 判断账号密码为空时
    if len(username)==0 or username==None:
        user_mess.update({"code":1,"message":"请输入正确的用户名以及密码!!!"})
        return user_mess
    if len(password)==0 or password==None:
        user_mess.update({"code":1,"message":"请输入正确的用户名以及密码!!!"})
        return user_mess
# 进行校验判断
    for user_u in user_list:
        if user_u.get("account")==username and user_u.get("password")==password:
            user_mess.update({"code":0,"message":"登录成功！","user_List":user_u})
            return user_mess
# 账户名或者密码错误的情况
    user_mess.update(({"code":1,"message":"请输入正确的用户名以及密码!!!"}))
    return user_mess

#  调用
# username=input("请输入用户名：")
# password=input("请输入密码：")
# print(Delu(username,password))


class User():
    # 增加
    def Add(self,username,password,**kwargs):
        user_dict={}
        user_dict["account"]=username
        user_dict["password"]=password
        user_dict.update(**kwargs)

        user_list.append(user_dict)
        add_data_from_file("user_data",user_list)
        user_mess.update({"message":"用户添加成功","add_time":datetime.now()})
    # 查询
    def Query(self,username):
        if user_mess.get("code")!=0:
            user_mess.update({"code":11,"message":"您还没有登录，请先登录！！！"})
            return user_mess
        # 输入正确的用户名进行查询，支持模糊查询


        #存放不包含密码的返回信息
        user_mes= []
        for user_u1 in user_list:
            account=user_u1.get("account")
            if username in account:
                user_u1.pop("password")
                user_mes.append(user_u1)

       # 判断新列表中是否有数值，有数据更新在信息中
        if user_mes:
            user_mess.update({"message":"查询成功！！！","user_list":user_mes})
            return user_mess
       # 未查到用户
        user_mess.update({"code": 12, "message": "查询失败，请检查用户名！！！"})
        return user_mess






    # username = input("请输入用户名：")
    # print(Query(username))

if __name__ == '__main__':
    # 定义一个函数用于选择模式

    flag=True
    while flag:
            choose=input(("==============================="
                    "\n请选择模式,输入对应编号选择："
                    "\n 1):按1选择登录："
                    "\n 2):按2选择查询："
                    "\n 3):按3进行添加："
                    "\n q): 退出操作:"
                    "\n 其它字符:) 未知操作，请重新输入:"))
            # 选择1进行登录操作
            if choose=="1":
                username = input("请输入用户名：")
                password = input("请输入密码：")
                print(Delu(username, password))
                print("="*30)
                continue
            # 选择2进行添加操作
            elif choose=="3":
                username = input("请输入要添加的用户名：")
                user = User()

                # 查询是否已存在
                get_user=user.Query(username)
                # if user_mess.get("code")!=0:
                #     user_mess.update({"message":"请先登录才能添加哦！！！"})
                if get_user.get("code")==12:

                    password = input("请输入用户密码:")
                    role = input("请输入用户角色:")
                    dep = input("请输入用户部门:")
                    user.Add(username,password,role=role,dep=dep)
                if get_user.get("code") == 0:
                    user_mess.update({"code":13,"message":"用户已存在，请勿重复添加"})




                print("=" * 30)
                continue
            elif choose=="2":
                username = input("请输入查询用户名：")
                user = User()
                print(user.Query(username))
                print("=" * 30)
                continue

            # 选择q
            elif choose in("q","quit"):
                flag =False
                print("退出成功！！！")
                # 如果输入特殊字符继续选择
            else:
                print("")
                print("=" * 30)
                continue
