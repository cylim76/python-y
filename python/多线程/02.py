"""
利用time函数，生成两个函数
顺序调用
计算总的计算世界

"""

import time
import _thread as thread
def loop1():
    print("Start loop 1 at:",time.ctime())

    time.sleep(4)
    print("End loop 1 at:",time.ctime())


def loop2():
    print("Start loop 2 at:", time.ctime())

    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Starting at:" , time.ctime())
    # 启动多线程的意思就是用多线程执行某个函数
    # 启动多线程函数为 start_new_thread
    # 参数有两个，一个是需要运行的函数名，第二个参数作为元组使用，为空则使用空元组
    # 注意，如果函数只有一个参数，需要在参数后有逗号
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    time.sleep(5)
    print("All done at:" , time.ctime())

if __name__ == '__main__':
    main()