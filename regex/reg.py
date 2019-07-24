import re
a=["(0):11(1) 12(2) 13(1)","(1):12(1) 11(2) 23(1)"]
pat="\(\d\)"
pat2="\d+?\(.\)"
istore="(?:\d+?)\((.)\)"
dev="(\d+?)\((?:.)\)"
for i in a:
    print(i)
    grp=re.match(pat, i)
    dev_istore=re.findall(pat2, i) # 0 , 1 
    istore_num=re.findall(istore,i)
    dev_num=re.findall(dev,i)
    print("grpid:",grp.group())
    print("dev_istore:",dev_istore)
    print("istore_num:",istore_num)
    print("dev_num:",dev_num)
    
web="www.google.com\n"
print(str.rstrip(web))  #str.rstrip 去掉\n
print(web)

m=re.match('oo','ooa222')
if m is not None: print(m.group())
pa="oo|ff|22"
m=re.search(pa ,'ffooa222oo')
if m is not None: print(m.group())
m=re.search(pa ,'ooffo oa2 22oo')
if m is not None: print(m.group())

mail="\w+@(\w+\.){0,2}\w+\.com(\.\w+)?"
#\w 字母和数字的集合
#\b 任何单词的边界  \B不是单词的边界
# * 是 0或者多次 ； + 是1次或者多次
# ？ 是0 或者1 次
m=re.match(mail, "yinhao2@w.w.leofs.com.cn")
if m is not None:print(m.group())

m=re.match("(\w+)(-)(\d+)", "a1aa-123", 0)
if m is not None :
    print(m.group(3))
    print(m.groups())

#findall  finditer 查找每一次出现的位置
str="charchar hahchar"       
ret=re.findall("char", str, 0)
print(ret) ##返回列表

#finditer 返回在对象中迭代
str="charchar hahchar"       
it=re.finditer(r"(ch\w)", str, re.I)



Test1="Ab, Bc, Cd"
print(re.split(", ", Test1))

telnum='176061196115645222'
print(re.fullmatch("[1]{1}[0-9]{10}",telnum))
print(re.match("[1]{1}[0-9]{10}",telnum))
m=re.search("[1]{1}[0-9]{3}",telnum)
print(m)
m=re.findall("[1]{1}[0-9]{3}",telnum)
print(m)
