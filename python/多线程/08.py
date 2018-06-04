import threading
import time

def loop1():
    print("Start loop 1 at:" , time.ctime())
    time.sleep(4)
    print("End loop 1 at:" , time.ctime())

def loop2():
    print("Start loop 2 at:" , time.ctime())
    time.sleep(2)
    print("End loop 2 at:" , time.ctime())

def loop3():
    print("Start loop 3 at:" , time.ctime())
    time.sleep(5)
    print("End loop 3 at:" , time.ctime())

def main():
    print("Starting at:" , time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    t1.setName("THR_1")
    t1.start()

    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop2, args=())
    t1.setName("THR_2")
    t1.start()

    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop3, args=())
    t1.setName("THR_3")
    t1.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是： {0}".format(thr.getName()))
    print("正在运行的子线程数量为 {0}".format(threading.activeCount()))
    print("All done at:" , time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)