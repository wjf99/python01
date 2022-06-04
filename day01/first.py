'''
print('HELLO')
# type
print(type(123)) #<class 'int'>
print(type('123')) #<class 'str'>
a=128
b=128
print(a is b)

#用while打印1到5的和
sum=0
i=0
while i<=5:
    sum=sum+i
    i+=1
print(sum)

for i in range(1,11):
    if i==7:
        continue
    print(i)
'''


list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2 == 0:
        print(i)
