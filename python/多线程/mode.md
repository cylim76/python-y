# 环境
- xubuntu 16.04
- anaconda
- pycharm
- Python 3.6
- https：//www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程

- 程序： 一堆代码以文本形式存放入一个文件
- 进程： 程序运行的一个状态
    - 包含地址控件，内存，数据栈等
    - 每个进场有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程： 
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题

- 全局解释器锁：（GIL）
    - Python代码执行是由Python虚拟机控制
    - 在主循环中之内更有一个控制线程在执行

- Python包：
    - thread：有问题，不好用，Python改成了_thread
    - threading：通用的包
    
    - 案例01: 顺序执行，耗时长
    - 案例02： 该有多线程，使用_thread,使用时间短
    - 案例03： 多线程，穿数据
    
- threading的使用：
    - 直接利用threading.Thread生成Thread实现
        1. t =threading.Thread(target = xxx , args = (xxx,))
        2. t.start():启动多线程
        3. t.join() : 等待多线程执行结束
        4. 案例04
        5. 案例05：加入join后
        - 守护线程-daemon
            - 如果在程序将子线程设置为守护线程，则子线程会在主线程结束时退出
            - 一般认为，守护线程不重要或者补运行离开主线程独立运行
            - 守护线程案例能否有效果跟环境有关
            - 案例06非守护
            - 07 守护
        - 线程常用属性
            - threading.currentThread :返回当前线程变量
            - threading.enumerate:返回一个包含正在运行的线程list，正在运行的线程是指启动之后，结束之前
            - threading.activeCount:返回正在运行的线程数量，效果跟 len(threading.enumerate)相同
            - thr.setName:给线程设置名字
            - thr.getName:得到线程的名字
    - 直接继承自threading.Thread
        - 需要继承Thread
        - 重写run函数
        - 类实例直接运行
        - 案例09
        - 案例10 
            
            
            