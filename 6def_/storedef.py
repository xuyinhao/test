#任意数量的参数
# def printp(v1,**pa):
#     print(v1,pa)
#
# # printp("testing",bb=9,n=9)
#
# printp('1',aa=1,m=0)
# # printp(1,2,3,4,5)

def story(**wds):
    print("there is a(n) %(job)s and  %(name)s" % wds)
def power(x,y,*others):
    if others:
        print("Reveived too much arguments: ",others)
    else:
        print(pow(x,y))
def interval(start,stop=None,step=1):
    if stop is None:
        start,stop=0,start    #start=0 stop=start
    result=[]
    i=start
    while i < stop  :
        result.append(i)
        i+=step
    return result
print(interval(6))
story(job='apple',name='Eric')
power(2,3,78,9)
power(2,3)


