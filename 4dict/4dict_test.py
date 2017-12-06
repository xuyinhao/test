#字典 dict 映射mapping
#1.创建字典
# dstr={'a':'1','b':'2','c':'3'}
# print(dstr['b'])
#
# dstr1=[('name','gab'),('age',24)]
# ndstr1=dict(dstr1)
# print(ndstr1)
#
# dstr2=dict(name='gg',age=23)
# print(dstr2)

#2.基本字典操作
# print(len(dstr2))  #len(d) 键值对个数
# print(dstr2['name'])  #特定键 对应的value
# dstr2['sex']='man'
# print(dstr2)
# dstr2['name']='ggnew'   #键 赋值，或者新添加
# print(dstr2)
# del dstr2['sex']        #删除某个键
# print(dstr2)
# print('name' in dstr2)   # 判断某个键是否存在

#3.字典格式化字符串
#可以在 %（key）s 来打印 value值
# dt={'a':'1','b':'2','c':'3'}
# print('c\'s value is %(c)s ' %dt)
# tmp='''
# title
# %(title)s
# digital
# %(digital)d
# '''
# print(tmp)
# data={'title':'python','digital':22222222222}
# print(tmp%data)

#4 字典的方法
