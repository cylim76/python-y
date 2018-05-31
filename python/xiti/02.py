#python3

'''
模块功能
有个hello函数
一个打印语句
'''

class Student():
    def __init__(self,name='Noname',age=18):
        self.name=name
        self.age=age

    def say(self):
        print("My name is {0}".format(self.name))

def hello():
    print("Hi")
# 程序入口
if __name__ == '__main__':
    print("欢迎来到图灵学院")