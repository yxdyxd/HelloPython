#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('hello world')

# name = input('please enter your name: ')
# print('hello,', name)

# print(type(name))

# age = 4
#
# if age >= 18:
#     print ("123")
# else:
#     print ("456")
#
# a = 123 #a 是整数
# print(a)
# b = 'ABC' #b为字符串
# print(b)

# 导入实除法模块后的结果即为浮点数
# from __future__ import division
# a = 10 / 3
# print(a)


# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print (power(3, 3))


# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print ('power2 = %d' % power(5))
#
# # 多个占位符
# s = "I am %s,age %d" % ('alex', 18)
# print(s)

# 不添加默认的参数
# def enroll(name, gender):
#     print('name: %s' % name)
#     print('gender: %s' % gender)
#     return
#
#
# enroll('jack', 'boy')


# 添加默认的参数
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name: %s' % name)
#     print('gender: %s' % gender)
#     print('age: %d' % age)
#     print('city: %s' % city)


# enroll('Lucy', 'girl')
# enroll('Bod', 'Boy', 17)
# enroll('Adam', 'Boy', 20, city='Tianjin')
# enroll('jack', 'boy', 20, 'Tianjin')

# 添加默认参数的坑
# def add_end(L=[]):
#     L.append('end')
#     return L


# 多次调用默认函数
# print(add_end())
# print(add_end())
# 此处打印，本应为一个'end'，结果打印了三个
# 定义默认参数：默认参数必须指向不变对象
# print(add_end())


# 默认参数的正确写法
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
#
# print(add_end())
# print(add_end())
# print(add_end())

# 可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# # print(calc([1, 2, 3]))
# # print(calc([1, 3, 5, 7]))
#
# # print(calc([]))
# # 此处传入的参数应为空list或tuple，传入为空会报错
# # print(calc())
#
# # 1.重写此方法，在number前加上*号，将接受的参数变为可变参数
# # 2.加上*号，接收到的number依然是list或者tuple，函数代码完全不变
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# # print(calc(1, 2, 3))
# # print(calc())
#
# # 假如传入的为list或者tuple，加上*即可
# # *nums表示把nums这个list的所有元素作为可变参数传进去
# nums = [1, 2, 3]
#
#
# # print(calc(*nums))
#
#
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, \
#           'other:', kw)
#
#
# # person('jack', 30)
# # person('tom', 28, city='Beijing')
# # person('bob', 12, gender='boy', city='Tianjin')
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
#
#
# # 注意kw获得的dict是extra的一份拷贝，对kw的改动\
# # 不会影响到函数外的extra，作用是可以添加额外的参数
# # person('mike', 23, **extra)
#
#
# # 关键字参数
# # def person(name, age, **kw):
# #     if 'city' in kw:
# #         # 有city参数
# #         pass
# #     if 'job' in kw:
# #         # 有job参数
# #         pass
# #     print('name:%s' % name, 'age:%d' % age, 'other:', kw)
#
# # person('jack', 21, city='Beijing', addr='Chaoyang',\
# #        zipcode=12345)
#
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# # person('jack', 24, city='Beijing', job='Engineer')
#
#
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
#
# # 此处调用时，需要参数名（city， job），否则就会报错
# # person('jack', 25, city='Beijing', job='teacher')
#
#
# # 添加默认的关键字参数
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
#
#
# # person('mike', 32, job='student')
# # 也可以在外部更改默认的关键字参数，可以传入空值
# # person('mike', 21, city='Tianjin', job='student')
# # person('mike', 21, city='', job='student')
#
#
# # 参数的组合：
# # 定义参数的顺序为：必选参数、默认参数、可变参数、
# # 命名关键字参数、关键字参数
#
# # 定义一个参数，包含上述若干种参数
#
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, \
#           'kw =', kw)
#
#
# # f1(1, 2)
# # f1(1, 2, c=3, city='Beijing')
# # f1(1, 2, 3, '1', '2')
# # f1(1, 2, 0, 1, 2, 3, city='Beijing')
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a2 =', a, 'b =', b, 'c =', c, 'd =', d,\
#           'kw =', kw)
#
#
# # f2(3, 4, 5, d=6, student=23)
#
# # 通过tuple或者dict也可以调用上述函数
# args = (1, 2, 3, 4)
# kw = {'q': 00, 'x': 'y'}
#
# # f1(*args, **kw)
#
# args = (1, 2, 3)
# kw = {'d': 00, 'x': 'y'}
# # f2(*args, **kw)
#
#
# def product(x, y):
#     return x * y
#
#
# def product(a, *args):
#     sum = a
#     for n in args:
#         sum = sum*n
#     return sum
#
#
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
#
#
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


#


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# print(fact(1))
# print(fact(5))
# print(fact(1000))

# 上边的方式会造成栈的溢出
# 解决方法是通过尾递归优化，在函数返回是，调用本身，并且不包含表达式

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(10, 1))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


# 递归赋值（话说网上真的是能人辈出）
print(move(3, 'A', 'B', 'C'))