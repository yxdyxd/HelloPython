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
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# print(calc([1, 2, 3]))
# print(calc([1, 3, 5, 7]))

# print(calc([]))
# 此处传入的参数应为空list或tuple，传入为空会报错
# print(calc())

# 1.重写此方法，在number前加上*号，将接受的参数变为可变参数
# 2.加上*号，接收到的number依然是list或者tuple，函数代码完全不变
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# print(calc(1, 2, 3))
# print(calc())

# 假如传入的为list或者tuple，加上*即可
# *nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]


# print(calc(*nums))


def person(name, age, **kw):
    print('name: %s' % name, 'age: %d' % age, \
          'other: %s' % kw)


# person('jack', 30)
# person('tom', 28, city='Beijing')
# person('bob', 12, gender='boy', city='Tianjin')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# 注意kw获得的dict是extra的一份拷贝，对kw的改动\
# 不会影响到函数外的extra
# person('mike', 23, **extra)


# 关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:%s' % name, 'age:%d' % age, 'other:', kw)

# person('jack', 21, city='Beijing', addr='Chaoyang',\
#        zipcode=12345)

def person(name, age, *, city, job):
    print(name, age, city, job)



