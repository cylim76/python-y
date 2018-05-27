import random,math
# 输入函数
num =input("请输入一个三位数：")
# 检测输入是否为纯数字

if num.isdigit() and 100<=int(num)<1000:
    if int(num)>random.randint(100,1000):
        print("yes")
    else:
        print("No")

else:
    print("请按照规定输入")
