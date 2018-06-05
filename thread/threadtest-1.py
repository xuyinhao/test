##直接对一个函数进行 多线程
import time,threading
def TestPrint(name):
    print(name)
    time.sleep(2)

if __name__ == '__main__':
    # TestPrint("test1")
    # TestPrint("Test2")
    ##创建 线程
    for i in range(4):
        t=threading.Thread(target=TestPrint,args=(i,))
        t.start()
        #t.join()
    print("End")