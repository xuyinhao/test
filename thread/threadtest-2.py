##新建一个线程类
import time
import threading
class NewThread(threading.Thread):
    '''
    Test
    '''
    def __init__(self,name):
        ##显式的调用父类的 初始化
        super(NewThread,self).__init__()
        self.name=name
        # print(self.name)
    def getResult(self):
        return self.res
        
    def run(self):
        print(self.name)
        threading.Thread.setName(self,"thread"+self.name)
        print("name:",threading.Thread.getName(self))
        time.sleep(2)
        print(self.name,"e")
        self.res="OK"
        
def ThreadStart1():
    #没有join等待线程结束
    for i in range(4):
        t=NewThread(i)
        t.start()
def ThreadStart2():
    ##添加join 等待线程结束才执行下面的语句
    threads=[]
    for i in range(4):
        th=NewThread(i)
        threads.append(th)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        print(t.getResult())
    print("End")

if __name__ == '__main__':
    ThreadStart2()
    pass