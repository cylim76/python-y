import threading
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
    print("Start at" , time.ctime())
    t1 = threading.Thread(target=loop1,args=("杨鏊腾",))
    t1.start()

    t2 = threading.Thread(target=loop2,args=("520","王雯雯"))
    t2.start()

    t1.join()
    t2.join()
    print("All done at " , time.ctime())

if __name__ == '__main__':
    main()
