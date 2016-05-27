# -*- coding: utf-8 -*-
# 定义函数 def
# def my_abs(x):
#     if x>=0:
#         return x;
#     else:
#         return -x;
#
# s=int(input("input a number:"));
# # input输入的是string要转化为int
# print(my_abs(s));
# 如果函数返回的值个数不定该如何解决，比如一元二次方程,返回tuple需要多少用多少
def buding(a):
    if a>0:
        return 1;
    if a==0:
        return 2,3;
    if a<0:
        return 4,5,6;

a=int(input("print a number:"));
c=buding(a);
print(c)