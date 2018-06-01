# #下面列出了Python 3中其他不再返回列表的常用函数和方法：
# zip()
# map()
# filter()
# 字典的.key()方法
# 字典的.value()方法
# 字典的.item()方法
# #map 函数 将序列中的元素全部传递给
# a=map(str,range(10))
# print(list(a))
#--2


#filter 函数可以基于一个返回布尔值的函数对元素进行过滤
# def func(x):
#     return x.isalnum()   #字符串是否由字母和数字组成
#
# seq=['foo','x4','?!','***','a90']
# b=filter(func,seq)
# print(list(b))

#---
#seq=['aa','0-','op1']
# aa=filter(lambda x: x.isalnum(),seq)  #lambda是个匿名函数
# print(list(aa))

##reudce 会将序列的前两个元素与给定的函数联合使用,并将他们返回值和第三个函数继续联合使用\
# from functools import reduce
# number=[1,2,3,4,5,6,7,8,9,10]
# bb=reduce(lambda x,y: x+y , number)
# print(bb)