import sys
#文件标准输入 cat index|python file.py
# text=sys.stdin.read()
# word=text.split()
# wordcount=len(word)
#
# print(wordcount)

#seek  tell
#对文件迭代
def process(str):
    print("process string :%s" %str)
f=open('index','r')
##按字节操作
while True:
    char=f.read(1)
    if not char : break
    process(char)
f.seek(0)
#按行操作
while True:
    line=f.readline()
    if not line : break
    process(line)
f.close()

##读取所有内容
f=open('index')
for char in f.read():
    process(char)
f.seek(0)
for line in f.readlines():
    process(line)
f.close()

#fileinpit 已经包含了 打开文件
import fileinput
for line in fileinput.input('index'):
    process(line)

#文件对象可直接迭代

f=open('index')
for line in f:
    process(line)
