import random
#1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
'''a=int(input("请输入整数a:"))
b=int(input("请输入整数b:"))
c=int(input("请输入整数c:"))
d=int(input("请输入整数d:"))
print("的结果等于",a+b-c*d)'''
#2. 打印1~100内被3整除的所有数的和 。
import random

'''sum=0
for i in range(1,100):
    if i % 3 == 0:
        sum+=i
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for i in range(1,10):
    if i % 2 !=0:
        print(i)'''
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
'''sum=0
sum1=0
sum2=0
for i in range(1,100):
    if i % 2 == 0:
        sum1+=i
    else:
        sum2 += i
print("偶数和为",sum1)
print("奇数和为",sum2)
# 5. 求1+2+3+...+100的和
sum=0
for i in range(1,100):
    sum+=i
print(sum)
# 6. 判断一个数n能同时被3和5整除
n=int(input("请输入整数n:"))
if n % 3==0 and n % 5 == 0:
    print("n不能同时被3和5整除")
else:
    print("n不能同时被3和5整除")'''
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# a=int(input("请输入数字："))
# if a>=1 and a<=100:
#     print("猜对了")
# else:
#     print("猜错了")

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))
z = int(input("请输入第三个数："))
if x > y:
    if z > y:
        z,x=x,z
    else:
        if x < z:
            y,x=x,y




# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法
# 10. 将一个列表的数据复制到另一个列表中。
# list1=[1,2,3]
# list2=['a',"b","c"]
# for i in list2:
#     list1.append(i)
# print(list1)
# 11. 输出 9*9 乘法口诀表。
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# str=input("请输入一行字符：")
# count1=count2=count3=count4=0
# for i in str:
#     if i.isalpha():
#         count1+=1
#     elif i.isspace():
#         count2+=1
#     elif i.isdigit():
#         count3+=1
#     else:
#         count4+=1
# print("英文字母的个数是",count1)
# print("空格的个数是",count2)
# print("数字的个数是",count3)
# print("其他字符的个数是",count4)

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。
# s = 0
# a = int(input("请输入几个数相加:"))
# for i in range(a):
#     print(i)


# num = int(input("请输入要相加的数字："))
# count = int(input("请输入要想加的个数："))
# sum=0
# s=0
# for i in range(1,count+1):
#     s+=num*10**(i-1)
#     sum+=s
# print(sum)

# 14. 题目：打印出如下图案（菱形）:
# a="*"
# for i in range(1,8,2):
#     b=(7-i)//2
#     print(" "*b+a*i+" "*b)
# for i in reversed(range(1,6,2)):
#     b = (7-i) // 2
#     print(" "*b+a*i+" "*b)

