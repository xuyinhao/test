##直接对一个函数进行 多线程
import time,threading
from random import randint
def TestPrint(value,thname):
    print(value,thname)
#     print(randint(1,5))
    time.sleep(randint(2,5))
    print(thname+"fineshed")
    

def ThreadStart3():
    from concurrent.futures import ThreadPoolExecutor
    threads=[]
   
    with ThreadPoolExecutor(3) as exc:
        for i in range(10):
            a=exc.submit(TestPrint,i,str(i)+"name")
            threads.append(a)
            
    
if __name__ == '__main__':
    # TestPrint("test1")
    # TestPrint("Test2")
    ##创建 线程
#     for i in range(4):
#         t=threading.Thread(target=TestPrint,args=(i,))
#         t.start()
        #t.join()
    ThreadStart3()
    print("End")