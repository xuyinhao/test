import time,threading

class NewThread(threading.Thread):
    def __init__(self,arg):
        super(NewThread,self).__init__()
        self.arg=arg
    def run(self):

        print("Eeee")
        time.sleep(0.1)
        global enm
        lock.acquire()
        enm+=1
        print(enm)
        lock.release()
        time.sleep(1)

if __name__ == '__main__':
    enm=0
    lock=threading.Lock()
    # lock.acquire()
    threads=[]
    for i in range(10):
        t=NewThread(i)
        threads.append(t)
    for t in threads:
        t.start()
    for t in  threads:
        t.join()
