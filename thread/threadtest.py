from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock=Lock()
MAX=5
candyray=BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print("Refilling Candy...")
    try:
        candyray.release()
    except ValueError:
        print("Full,skipping")
    else:
        print("ok")
    lock.release()
    
def buy():
    lock.acquire()
    print("Buying candy...")
    if candyray.acquire(False): #False,acquire（也就是 -1）时，如果失败则立即返回false
        print("ok")
    else:
        print("empty,skipping")
    lock.release()
    
def producter(loops):
    print("refill loops,",loops)
    for i in range(loops):
        refill()
        sleep(randrange(3))
def consumer(loops):
    print("buy loops",loops)
    for i in range(loops):
        buy()
        sleep(randrange(3))
def _main():
    print("staring at:",ctime())
    nloops=2
    print("The candy machine full with %d bars!"%MAX)
    Thread(target=consumer,args=(randrange(nloops,nloops+MAX+10),)).start()
    Thread(target=producter,args=(nloops,)).start()
    
@register
def _atexit():
    print("All done at:",ctime())
    
    
if __name__ == '__main__':
    _main()