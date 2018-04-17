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

