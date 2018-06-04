#from math   import pi
#f 实数（浮点数）    取3个小数点
#print("mm:%.3f" % pi)

#Templat 变量赋值
# from string import Template
# s=Template("$x xixixi $x")
# ss=s.substitute(x='hello')
# print(ss)
# # #还可以使用字典
# s1=Template("$thing is $most")
# sd={}
# sd['thing']='this'
# sd['most']='a dog'
# sdd=s1.substitute(sd)
# print(sdd)

#
# makestrans()
# 语法: str.maketrans(intab, outtab]);
# Python
# maketrans()
# 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 注：两个字符串的长度必须相同，为一一对应的关系。
#
# Python3.4
# 已经没有string.maketrans()
# 了，取而代之的是内建函数:
# bytearray.maketrans()、bytes.maketrans()、str.maketrans()

# intab = "abcd"
# outtab = "1234"
# str_trantab = str.maketrans(intab, outtab)
# test_str = "abcd"
# print(test_str.translate(str_trantab))   #注意translate

#-------------
#split 可以用把一行按照特定字符分开
# print('1+2+3 2'.split('+'))
#join 把字符之间加上特定字符
# print('++'.join("1 2 34 4 4 3"))
#strip 把首尾 特定字符剔除
# print('  112 2 3 + 12+ 123 ++ +  '.strip(" +"))
#replace 替换特定的字符
# print("tee isee hello ".replace('ee','oo'))
#字符串的打印
# import string
# print(string.ascii_letters) #输出所有字符
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.printable) #输出所有可打印字符的字符串
# print(string.punctuation) #所有标点的字符串
# print(string.digits) #所有数字
# a=string.digits+string.ascii_uppercase
# print(a)
