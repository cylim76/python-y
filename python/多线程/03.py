import _thread as thread
import time

def loop1(in1):
    print("Start loop 1 at:" , time.ctime())
    print("我是参数" ,in1)
    time.sleep(4)
    print("End loop 1 at:" , time.ctime())

def loop2(in1,in2):
    print("Start loop 2 at:" , time.ctime())
    print("我是参数{0},和{1}".format(in1,in2))
    time.sleep(2)
    print("End loop 2 at:" , time.ctime())

def main():
    print("Start at:" , time.ctime())
    thread.start_new_thread(loop1,("杨鏊腾",))
    thread.start_new_thread(loop2,("王雯雯","520"))
    time.sleep(5)
    print("End at:" , time.ctime())

if __name__ == '__main__':
    main()
    