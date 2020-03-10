# candy 糖果机和信号量

from atexit import register
from random import randrange
from threading import  BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock=Lock()
MAX=5
candytray=BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('refill candy')
    try:
        candytray.release()
    except:
        print('full , skip')
    else:
        print('fill OK')
    lock.release()

def buy():
    lock.acquire()
    print("Buy candy")
    if candytray.acquire(False):
        print('ok')
    else:
        print('empty ,skip')
    lock.release()

def producer(loops):
    print("p %d" % loops)
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    print("c %d " % loops )
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting')
    nloops=randrange(2,6)
    print('THE MAX full with %d bars' % MAX)
    # Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2),)).start()

    Thread(target=producer,args=(nloops,)).start()


@register
def _atexit():
    print("all done at:",ctime())

if __name__ == '__main__':
    _main()