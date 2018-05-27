import math
'''
# print(math)
# celi()向上取整操作

print(math.ceil(5.6))
print(math.ceil(5.1))


# floor() 向下取整操作

print(math.floor(5.9))
# 查看系统保留关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)


#round() 四舍五入
print(round(5.5))
print(round(5))
#sqrt()开平方
print(math.sqrt(4))
print(math.sin(0.5))


#pow() 幂运算，计算幂的几次方,第一次是底数，第二个是指数

print(math.pow(4,3))
print(4**3)

# fabs() 对一个数值获取绝对值
print(math.fabs(-1))
print(math.fabs(6))

# abs(),获取绝对值,Python内置函数

print(abs(-1))
print(abs(6))

#fsun 对整个数列集合求和

print(math.fsum([1,4,5,6]))

#sun Python内置函数求和
print(sum([1,4,5,6]))





# math.modf(),讲一个浮点数拆分为整数和小数部分

print(math.modf(5.2))
help(math.modf)


#copysign()，将第二个数符号传递给第一个值
print(math.copysign(-2,2))


#打印自然对数e和pi的值
print(math.e)
print(math.pi)
'''

import random
'''
# random() 获取 0-1直接的随机小数 包含开始 ，不包含结尾

for i in range(10):
    print(random.random())
    print(random.randint(0,5))
    print(random.randrange(1,9,2))
    # random.randrange() 获取制定开始和结束之间的值，他可以制定间隔值
# choice() 随机获取列表的值
print(random.choice([1,5,6,7,8]))
list=[5,6,98,15]
print(list)
random.shuffle(list)
print(list)
'''
#uniform()-随机获取制定范围的值，（包括小数）
print(random.uniform(1,9))


