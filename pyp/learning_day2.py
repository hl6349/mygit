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
# 默认参数必须指向不变对象
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的
# 完成到模块