"""
定义一个学生类，来描述学生
"""
#定义一个空的类
class Student(object):
    #是一个空类，pass代表直接跳过
    #此时Python必须有
    pass

#定义一个对象
mingyue=Student()

#定义一个类，用来描述听Python的学生

class PyhtonStudent():
    name=None
    age=18
    coures = "Python"

    #需要注意
    # 1. def,doHomework的缩进层级
    # 2.系统默认一个参数self
    def doHomework(self):
        print("I 在做作业")

        return None
#对象实例化
yueyue= PyhtonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()
