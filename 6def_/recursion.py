##递归
##1 n阶乘
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(3))

##2. 幂
# def power(x,n):
#     if n == 1:
#         return x
#     else:
#         return x*power(x,n-1)
# print(power(3,3))

##二分法
# def search(seqe,num,lower,upper):
#     middle  = (lower+upper)//2
#     if num > seqe[middle]:
#         return search(seqe,num,middle+1,upper)
#     elif num == seqe[middle]:
#         return middle
#     else:
#         return search(seqe,num,lower,middle-1)
# seq=[12,13,14,15,16,17,18]
# seq.sort()
# a=search(seq,19,0,6)
# print(a)