# a = str(input("请输入："))
# b = str(input("请输入："))
# print("input获取的内容：",len(a+b))

# d= {}
# d.update(name = input("请输入:"))
# d.update(age = input("请输入:"))
# d.update(sex = input("请输入:"))
# print(d)

# dict1 = {}
# dict2 = {}
# list3 = ["张三","李四","王五","小黑","小白","小昂","小兰","小吕","小紫","小青"]
# i = 0
# while i < len(list3):
#     score = int(input("请输入成绩：")) 
#     if score >= 60:
#         dict1[list3[i]] = score
#         # print(dict1)
#     else:
#         dict2[list3[i]] = score
#         # print(dict2)
#     i = i+1
# print("大于60",dict1)
# print("小于60",dict1)
# for i in range(1,10):
#     for j in range(1,1+i):
#         print( j,"x", i,"=",i*j,end=" ")
#     print()


# for i in range(1,36):
#     print("绿灯亮",i,"次")
#     if i<=30:
#         print("红灯亮",i,"次")
#         if i<=3:
#             print("黄灯亮",i,"次")
    
# list1 = {"红灯":30,"绿灯":35,"黄灯":3}
# for i in list1:
#     for j in range(list1[i]):
#         print(i,j)






# name = input("请输入账号：")
# pwd = input("请输入密码：")
# if len(name)>=5 and len(name)<=8:
#     if name[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         if len(pwd)>=6 and len(name)<=12:
#             print("注册成功",{name:pwd})
#         else:
#             print("您输入的密码长度有误")
#     else:
#         print("您输入的账号首字母不是小写")
# else:
#     print("您输入的账号长度有误")


# text = input("请输入：")
# with open("日记.txt","w") as f:
#     f.write(text)

# try:
#     text = input("请输入：")
#     if text == "1":
#         print("结果为1")
# except Exception as e:
#     print("出错了")
"""
0-100之和
"""
# a= 0
# for i in range(101):
#     a = i +a
# print(a)

a = [1,6,4,2,67,32]
l = len(a)
for i in range(l):
    for j in range(l-1):
        if a[l-1-j]<a[l-2-j]:
            a[l-1-j],a[l-2-j] = a[l-2-j],a[l-1-j]
for i in a:
    print(i)