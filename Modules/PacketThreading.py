import time, threading

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中无法使用

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)  # current_thread()函数，它永远返回当前线程的实例。
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)  # 主线程实例的名字叫MainThread
t = threading.Thread(target=loop, name='LoopThread')  # 用LoopThread命名子线程
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 假定这是你的银行存款:
balance1 = 0
balance2 = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance1
    balance1 = balance1 + n
    balance1 = balance1 - n


def change_it2(n):
    # 先存后取，结果应该为0:
    global balance2
    balance2 = balance2 + n
    balance2 = balance2 - n


def run_thread(n):
    for i in range(2000000):
        change_it(n)


lock = threading.Lock()


def run_thread2(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it2(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))  # args为输入
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance1)  # 因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了
t1 = threading.Thread(target=run_thread2, args=(5,))  # args为输入
t2 = threading.Thread(target=run_thread2, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance2)


# 创建全局ThreadLocal对象:
local_school = threading.local()  # 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
