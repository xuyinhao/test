##直接对一个函数进行 多线程
import time,threading
def TestPrint(value,thname):
    print(value,"thread_name:%s " % thname)
    time.sleep(2)
    print(value, "thread_name:%s " % thname)

if __name__ == '__main__':
    # TestPrint("test1")
    # TestPrint("Test2")
    ##创建 线程
    for i in range(40):
        t=threading.Thread(target=TestPrint,args=(i,i))
        t.start()
        #t.join()
    print("End")