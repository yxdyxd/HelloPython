# # #!/usr/bin/env python3
# # # -*- coding: utf-8 -*-
# #
# # # print('hello world')
# #
# # # name = input('please enter your name: ')
# # # print('hello,', name)
# #
# # # print(type(name))
# #
# # # age = 4
# # #
# # # if age >= 18:
# # #     print ("123")
# # # else:
# # #     print ("456")
# # #
# # # a = 123 #a 是整数
# # # print(a)
# # # b = 'ABC' #b为字符串
# # # print(b)
# #
# # # 导入实除法模块后的结果即为浮点数
# # # from __future__ import division
# # # a = 10 / 3
# # # print(a)
# #
# #
# # # def power(x, n):
# # #     s = 1
# # #     while n > 0:
# # #         n = n - 1
# # #         s = s * x
# # #     return s
# # #
# # #
# # # print (power(3, 3))
# #
# #
# # # def power(x, n=2):
# # #     s = 1
# # #     while n > 0:
# # #         n = n - 1
# # #         s = s * x
# # #     return s
# # #
# # #
# # # print ('power2 = %d' % power(5))
# # #
# # # # 多个占位符
# # # s = "I am %s,age %d" % ('alex', 18)
# # # print(s)
# #
# # # 不添加默认的参数
# # # def enroll(name, gender):
# # #     print('name: %s' % name)
# # #     print('gender: %s' % gender)
# # #     return
# # #
# # #
# # # enroll('jack', 'boy')
# #
# #
# # # 添加默认的参数
# # # def enroll(name, gender, age=6, city='Beijing'):
# # #     print('name: %s' % name)
# # #     print('gender: %s' % gender)
# # #     print('age: %d' % age)
# # #     print('city: %s' % city)
# #
# #
# # # enroll('Lucy', 'girl')
# # # enroll('Bod', 'Boy', 17)
# # # enroll('Adam', 'Boy', 20, city='Tianjin')
# # # enroll('jack', 'boy', 20, 'Tianjin')
# #
# # # 添加默认参数的坑
# # # def add_end(L=[]):
# # #     L.append('end')
# # #     return L
# #
# #
# # # 多次调用默认函数
# # # print(add_end())
# # # print(add_end())
# # # 此处打印，本应为一个'end'，结果打印了三个
# # # 定义默认参数：默认参数必须指向不变对象
# # # print(add_end())
# #
# #
# # # 默认参数的正确写法
# # # def add_end(L=None):
# # #     if L is None:
# # #         L = []
# # #     L.append('END')
# # #     return L
# # #
# # #
# # # print(add_end())
# # # print(add_end())
# # # print(add_end())
# #
# # # 可变参数
# # # def calc(numbers):
# # #     sum = 0
# # #     for n in numbers:
# # #         sum = sum + n * n
# # #     return sum
# # #
# # #
# # # # print(calc([1, 2, 3]))
# # # # print(calc([1, 3, 5, 7]))
# # #
# # # # print(calc([]))
# # # # 此处传入的参数应为空list或tuple，传入为空会报错
# # # # print(calc())
# # #
# # # # 1.重写此方法，在number前加上*号，将接受的参数变为可变参数
# # # # 2.加上*号，接收到的number依然是list或者tuple，函数代码完全不变
# # # def calc(*numbers):
# # #     sum = 0
# # #     for n in numbers:
# # #         sum = sum + n * n
# # #     return sum
# # #
# # #
# # # # print(calc(1, 2, 3))
# # # # print(calc())
# # #
# # # # 假如传入的为list或者tuple，加上*即可
# # # # *nums表示把nums这个list的所有元素作为可变参数传进去
# # # nums = [1, 2, 3]
# # #
# # #
# # # # print(calc(*nums))
# # #
# # #
# # # def person(name, age, **kw):
# # #     print('name:', name, 'age:', age, \
# # #           'other:', kw)
# # #
# # #
# # # # person('jack', 30)
# # # # person('tom', 28, city='Beijing')
# # # # person('bob', 12, gender='boy', city='Tianjin')
# # #
# # # extra = {'city': 'Beijing', 'job': 'Engineer'}
# # #
# # #
# # # # 注意kw获得的dict是extra的一份拷贝，对kw的改动\
# # # # 不会影响到函数外的extra，作用是可以添加额外的参数
# # # # person('mike', 23, **extra)
# # #
# # #
# # # # 关键字参数
# # # # def person(name, age, **kw):
# # # #     if 'city' in kw:
# # # #         # 有city参数
# # # #         pass
# # # #     if 'job' in kw:
# # # #         # 有job参数
# # # #         pass
# # # #     print('name:%s' % name, 'age:%d' % age, 'other:', kw)
# # #
# # # # person('jack', 21, city='Beijing', addr='Chaoyang',\
# # # #        zipcode=12345)
# # #
# # # def person(name, age, *, city, job):
# # #     print(name, age, city, job)
# # #
# # #
# # # # person('jack', 24, city='Beijing', job='Engineer')
# # #
# # #
# # # def person(name, age, *args, city, job):
# # #     print(name, age, args, city, job)
# # #
# # #
# # # # 此处调用时，需要参数名（city， job），否则就会报错
# # # # person('jack', 25, city='Beijing', job='teacher')
# # #
# # #
# # # # 添加默认的关键字参数
# # # def person(name, age, *, city='Beijing', job):
# # #     print(name, age, city, job)
# # #
# # #
# # # # person('mike', 32, job='student')
# # # # 也可以在外部更改默认的关键字参数，可以传入空值
# # # # person('mike', 21, city='Tianjin', job='student')
# # # # person('mike', 21, city='', job='student')
# # #
# # #
# # # # 参数的组合：
# # # # 定义参数的顺序为：必选参数、默认参数、可变参数、
# # # # 命名关键字参数、关键字参数
# # #
# # # # 定义一个参数，包含上述若干种参数
# # #
# # # def f1(a, b, c=0, *args, **kw):
# # #     print('a =', a, 'b =', b, 'c =', c, 'args =', args, \
# # #           'kw =', kw)
# # #
# # #
# # # # f1(1, 2)
# # # # f1(1, 2, c=3, city='Beijing')
# # # # f1(1, 2, 3, '1', '2')
# # # # f1(1, 2, 0, 1, 2, 3, city='Beijing')
# # #
# # #
# # # def f2(a, b, c=0, *, d, **kw):
# # #     print('a2 =', a, 'b =', b, 'c =', c, 'd =', d,\
# # #           'kw =', kw)
# # #
# # #
# # # # f2(3, 4, 5, d=6, student=23)
# # #
# # # # 通过tuple或者dict也可以调用上述函数
# # # args = (1, 2, 3, 4)
# # # kw = {'q': 00, 'x': 'y'}
# # #
# # # # f1(*args, **kw)
# # #
# # # args = (1, 2, 3)
# # # kw = {'d': 00, 'x': 'y'}
# # # # f2(*args, **kw)
# # #
# # #
# # # def product(x, y):
# # #     return x * y
# # #
# # #
# # # def product(a, *args):
# # #     sum = a
# # #     for n in args:
# # #         sum = sum*n
# # #     return sum
# # #
# # #
# # # print('product(5) =', product(5))
# # # print('product(5, 6) =', product(5, 6))
# # # print('product(5, 6, 7) =', product(5, 6, 7))
# # # print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# # #
# # #
# # # if product(5) != 5:
# # #     print('测试失败!')
# # # elif product(5, 6) != 30:
# # #     print('测试失败!')
# # # elif product(5, 6, 7) != 210:
# # #     print('测试失败!')
# # # elif product(5, 6, 7, 9) != 1890:
# # #     print('测试失败!')
# # # else:
# # #     try:
# # #         product()
# # #         print('测试失败!')
# # #     except TypeError:
# # #         print('测试成功!')
# #
# #
# # #
# #
# #
# # # def fact(n):
# # #     if n == 1:
# # #         return 1
# # #     return n * fact(n - 1)
# # #
# # #
# # # # print(fact(1))
# # # # print(fact(5))
# # # # print(fact(1000))
# # #
# # # # 上边的方式会造成栈的溢出
# # # # 解决方法是通过尾递归优化，在函数返回是，调用本身，并且不包含表达式
# # #
# # # def fact(n):
# # #     return fact_iter(n, 1)
# # #
# # #
# # # def fact_iter(num, product):
# # #     if num == 1:
# # #         return product
# # #     return fact_iter(num - 1, num * product)
# # #
# # #
# # # print(fact_iter(10, 1))
# # #
# # #
# # # def move(n, a, b, c):
# # #     if n == 1:
# # #         print(a, '-->', c)
# # #     else:
# # #         move(n - 1, a, c, b)
# # #         move(1, a, b, c)
# # #         move(n - 1, b, a, c)
# # #
# # #
# # # # 递归赋值（话说网上真的是能人辈出）
# # # # print(move(3, 'A', 'B', 'C'))
# # #
# # #
# # # # 切片
# # # L = ['mike', 'bob', 'jack', 'lucy', 'tom']
# # # # 取出前三个元素
# # # print(L[0:3])
# # # # 如果包含第一个元素的话，可以将0省略
# # # print(L[:3])
# # # # 取出第二三个元素
# # # print(L[1:3])
# # # # 也可倒数切片，例如-1
# # # print(L[-2:])
# # # print(L[-2:-1])
# # #
# # # # 取数练习
# # # b = list(range(100))
# # # print(b[:10])
# # # print(b[-10:])
# # # print(b[10:20])
# # # # 前十个数，每隔两个取一个
# # # print(b[:10:2])
# # # # 所有数，每5个取一个
# # # print(b[::5])
# # # # 取出所有数
# # # # print(b[:])
# # # # 字符串也可用来切片
# # # # 但是针对字符串的截取，有各种的系统方法(例如，substring)
# # #
# # #
# # # str = '  hello  '
# # # print(str[:1])
# # #
# # #
# # # def trim(s):
# # #     if s[:1] == " ":
# # #         return trim(s[1:])
# # #     if s[-1:] == " ":
# # #         return trim(s[:-1])
# # #     return s
# # #
# # #
# # # if trim('hello  ') != 'hello':
# # #     print('测试失败!')
# # # elif trim('  hello') != 'hello':
# # #     print('测试失败!')
# # # elif trim('  hello  ') != 'hello':
# # #     print('测试失败!')
# # # elif trim('  hello  world  ') != 'hello  world':
# # #     print('测试失败!')
# # # elif trim('') != '':
# # #     print('测试失败!')
# # # elif trim('    ') != '':
# # #     print('测试失败!')
# # # else:
# # #     print('测试成功!')
# #
# #
# # # d = {'a': 1, 'b': 2, 'c': 3}
# # # # Python中的遍历循环，称之为迭代
# # # # 迭代dict中的key
# # # for key in d:
# # #     print(key)
# # #
# # # # 迭代dict中的Value
# # # for value in d.values():
# # #     print(value)
# # #
# # # # 迭代dict中的Value和key
# # # for k, v in d.items():
# # #     print(k, v)
# # #
# # # # 字符串也可以迭代
# # # for ch in 'ABC':
# # #     print(ch)
# # #
# # # # 判断一个对象是否可迭代
# # # from collections import Iterable
# # # print(isinstance('abc', Iterable))
# # # print(isinstance([1, 2, 3], Iterable))
# # # # 整数不能迭代
# # # print(isinstance(123, Iterable))
# # #
# # # # Python内置的enumerate函数可以把一个list变成索引-元素对
# # # for i, value in enumerate(['A', 'B', 'c']):
# # #     print(i, value)
# # #
# # # for x, y in ([1, 1], [2, 4], [3, 9]):
# # #     print(x, y)
# # #
# # #
# # # # 请使用迭代查找一个list中最小和最大值，并返回一个tuple
# # # def findMinAndMax(L):
# # #     if L == []:
# # #         return (None, None)
# # #     else:
# # #         MIN = L[0]
# # #         MAX = L[0]
# # #         for X in L:
# # #             if MIN >= X:
# # #                 MIN = X
# # #             elif MAX <= X:
# # #                 MAX = X
# # #         return (MIN, MAX)
# # #
# # #
# # # if findMinAndMax([]) != (None, None):
# # #     print('测试失败!')
# # # elif findMinAndMax([7]) != (7, 7):
# # #     print('测试失败!')
# # # elif findMinAndMax([7, 1]) != (1, 7):
# # #     print('测试失败!')
# # # elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
# # #     print('测试失败!')
# # # else:
# # #     print('测试成功!')
# #
# #
# # # print(list(range(1, 11)))
# # # # 列表生成式，快速生成list
# # #
# # # L = []
# # # for x in range(1, 11):
# # #     L.append(x * x)
# # # print(L)
# # #
# # # #在列表生成式中，可以使用运算式，来得到自己想要的list
# # # print([x*x for x in range(1, 11)])
# # #
# # # # or循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
# # # print([x*x for x in range(1, 11) if x % 2 ==0])
# # #
# # # # 还可以使用两层循环，可以生成全排列
# # # print([m + n for m in 'ABC' for n in 'XYZ'])
# # #
# # # # 导入os模块
# # # import os
# # # # os.listdir可以列出文件和目录
# # # print([d for d in os.listdir('.')])
# # #
# # # # for循环其实可以同时使用两个甚至多个变量
# # # # 比如dict的items()可以同时迭代key和value
# # # d = {'x': 'A', 'y': 'B', 'z': 'C'}
# # # for k, v in d.items():
# # #     print(k, '=', v)
# # #
# # # # 列表生成式也可以使用两个变量来生成list
# # # print([k + '=' + v for k, v in d.items()])
# # #
# # # # 把一个list中所有的字符串变成小写
# # # L = ['Hello', 'World', 'IBM', 'Apple']
# # # print([s.lower() for s in L])
# # # # 把一个list中所有的字符串变成大写
# # # print([s.upper() for s in L])
# # #
# # # # 使用内建的isinstance函数可以判断一个变量是不是字符串
# # # x = 'abc'
# # # y = 123
# # # z = ''
# # # print(isinstance(x, str))
# # # # 也可用来判断是否是数字
# # # print(isinstance(y, int))
# # # # 判断是否为空
# # # print(isinstance(z, str))
# # #
# # # # 修改列表生成式，通过添加if语句保证列表生成式能正确地执行
# # # L1 = ['Hello', 'World', 18, 'Apple', None]
# # #
# # # L2 = [s.lower() for s in L1 if isinstance(s, str)]
# # #
# # # # 测试:
# # # print(L2)
# # # if L2 == ['hello', 'world', 'apple']:
# # #     print('测试通过!')
# # # else:
# # #     print('测试失败!')
# #
# #
# # # L = [x*x for x in range(10)]
# # # # print(L)
# # # g = (x*x for x in range(10))
# # # # 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# # # # 创建L和g的区别仅在于最外层的[]和()
# # # # L是一个list，而g是一个generator
# # # # generator并没有创建一个完整的数组，而是在不断的调用中生成
# # # # 主要的目的在于节省空间
# # # # print(g)
# # #
# # # #打印g中的所有元素
# # # # for n in g:
# # # #     print(n)
# # #
# # # # generator非常强大。如果推算的算法比较复杂
# # # # 用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# # # def fib(max):
# # #     n, a, b = 0, 0, 1
# # #     while n < max:
# # #         print(b)
# # #         a, b = b, a + b
# # #         n = n + 1
# # #     return 'done'
# # #
# # # # fib(6)
# # #
# # # # 修改上边函数为generator
# # # # 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# # # def fib(max):
# # #     n, a, b = 0, 0, 1
# # #     while n < max:
# # #         yield b
# # #         a, b = b, a + b
# # #         n = n + 1
# # #     return 'done'
# # #
# # #
# # # f = fib(6)
# # # print(f)
# # # # 这是定义generator的另一种方法。如果一个函数定义中包含yield关键字
# # # # 那么这个函数就不再是一个普通函数，而是一个generator
# # # # for n in fib(6):
# # # #     print(n)
# # #
# # # # 捕获错误的发生
# # # # g = fib(6)
# # # # while True:
# # # #     try:
# # # #         x = next(g)
# # # #         print('g:', x)
# # # #     except StopIteration as e:
# # # #         print('Generator return value:', e.value)
# # # #         break
# # #
# # #
# # # def triangles():
# # #     tr = [1]
# # #     while True:
# # #         yield tr
# # #         ntr = tr[:]
# # #         for i in range(len(tr)):
# # #             if i == 0:
# # #                 ntr[i] = 1
# # #             else:
# # #                 ntr[i] = tr[i] + tr[i-1]
# # #         ntr.append(1)
# # #         tr = ntr[:]
# # #
# # #
# # # n = 0
# # # results = []
# # # for t in triangles():
# # #     print(t)
# # #     results.append(t)
# # #     n = n + 1
# # #     if n == 10:
# # #         break
# # # if results == [
# # #     [1],
# # #     [1, 1],
# # #     [1, 2, 1],
# # #     [1, 3, 3, 1],
# # #     [1, 4, 6, 4, 1],
# # #     [1, 5, 10, 10, 5, 1],
# # #     [1, 6, 15, 20, 15, 6, 1],
# # #     [1, 7, 21, 35, 35, 21, 7, 1],
# # #     [1, 8, 28, 56, 70, 56, 28, 8, 1],
# # #     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# # # ]:
# # #     print('测试通过!')
# # # else:
# # #     print('测试失败!')
# #
# #
# # # from collections import Iterable
# # #
# # # # 可以直接作用于for循环的对象统称为迭代对象：Iterable
# # # # 使用isinstance()判断一个对象是否为Iterable
# # # # print(isinstance([], Iterable))
# # # # print(isinstance(123, Iterable))
# # # # print(isinstance((x for x in range(10)), Iterable))
# # #
# # # # 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# # # # 可以使用isinstance()判断一个对象是否是Iterator对象
# # # from collections import Iterator
# # #
# # #
# # # # print(isinstance('abc', Iterator))
# # # # print(isinstance((x for x in range(10)), Iterator))
# # # # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# # # # print(isinstance(iter([]), Iterator))
# # # # print(isinstance(iter('abc'), Iterator))
# # #
# # #
# # # # 函数名也是变量，可以通过赋值把一个整数赋值给函数名
# # # # 既然变量可以指向函数，函数的参数能接收变量
# # # # 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# # # # 列举一个简单的高阶函数
# # # def add(x, y, f):
# # #     return f(x) + f(y)
# # #
# # #
# # # # print(add(-5, 6, abs))
# # #
# # #
# # # # map()函数接收两个参数，一个是函数，一个是Iterable
# # # # 一个函数f(x)=x2(x的平方)
# # # # 把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
# # # def f(x):
# # #     return x * x
# # #
# # #
# # # r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # # # print(list(r))
# # #
# # # # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# # # # 这个函数必须接收两个参数
# # # # reduce把结果继续和序列的下一个元素做累积计算
# # # # 等价于:reduce(f,[x1, x2, x3, x4]) = f(f(f(x1, x2), x3),x4)
# # # from functools import reduce
# # #
# # #
# # # def add(x, y):
# # #     return x + y
# # #
# # #
# # # # print(reduce(add, [1, 3, 5, 7, 9]))
# # #
# # #
# # # def fn(x, y):
# # #     return x * 10 + y
# # #
# # #
# # # print(reduce(fn, [1, 3, 5, 7, 9]))
# # #
# # #
# # # def charm2num(s):
# # #     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, \
# # #               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# # #     return digits[s]
# # #
# # #
# # # # print(reduce(fn, map(charm2num, '13579')))
# # # #
# # # # print(charm2num('5'))
# # # # print(list(map(charm2num, '12345')))
# # #
# # # DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, \
# # #           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# # #
# # #
# # # def str2int(s):
# # #     def fn(x, y):
# # #         return x * 10 + y
# # #
# # #     def charm2num(s):
# # #         return DIGITS[s]
# # #
# # #     return reduce(fn, map(charm2num, s))
# # #
# # #
# # # # print(str2int('123456'))
# # #
# # #
# # # # 继续简化
# # # def charm2num(s):
# # #     return DIGITS[s]
# # #
# # #
# # # def str2int(s):
# # #     return reduce(lambda x, y: x * 10 + y, map(charm2num, s))
# # #
# # #
# # # # print(str2int('1234'))
# # #
# # #
# # # def normalize(name):
# # #     str1 = name[:1].upper() + name[1:].lower()
# # #     return str1
# # #
# # #
# # # L1 = ['adam', 'LISA', 'barT']
# # # L2 = list(map(normalize, L1))
# # # print(L2)
# # #
# # #
# # # def prod(L):
# # #     def sum1(x, y):
# # #         return x * y
# # #
# # #     return reduce(sum1, L)
# # #
# # #
# # # print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# # # if prod([3, 5, 7, 9]) == 945:
# # #     print('测试成功!')
# # # else:
# # #     print('测试失败!')
# # #
# # #
# # # def str2float(s):
# # #     return reduce(lambda x, y: x * 10 + y, \
# # #                   map(int, s.split('.')[0])) + \
# # #            reduce(lambda x, y: x / 10 + y, \
# # #                   map(int, s.split('.')[-1][::-1])) / 10
# # #
# # #
# # # print('str2float(\'123.456\') =', str2float('123.456'))
# # # if abs(str2float('123.456') - 123.456) < 0.00001:
# # #     print('测试成功!')
# # # else:
# # #     print('测试失败!')
# #
# #
# # def is_odd(n):
# #     return n % 2 == 1
# #
# #
# # # filter()函数用于过滤序列
# # # filter()函数也是用来接受两个参数，和map()函数一样是作用于
# # # 序列中的每个元素，但是根据返回的True和false来确定是否保留元素
# # print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# #
# #
# # # strip() 方法用于移除字符串头尾指定的字符（默认为空格)
# # def not_empty(s):
# #     return s and s.strip()
# #
# #
# # print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# #
# #
# # # 用filter求素数
# # def _odd_iter():
# #     n = 1
# #     while True:
# #         n = n + 2
# #         yield n
# #
# #
# # # 筛选序列
# # def _not_divisiable(n):
# #     return lambda x: x % n > 0
# #
# #
# # def primes():
# #     yield 2
# #     it = _odd_iter()  # 初始序列
# #     while True:
# #         n = next(it)  # 返回序列的第一个数
# #         yield n
# #         it = filter(_not_divisiable(n), it)
# #
# #
# # for n in primes():
# #     if n < 1000:
# #         pass
# #         # print(n)
# #     else:
# #         break
# #
# #
# # def is_palindrome(n):
# #     return str(n) == str(n)[::-1]
# #
# #
# # output = filter(is_palindrome, range(1, 1000))
# # print('1~1000:', list(output))
# # if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
# #     print('测试成功!')
# # else:
# #     print('测试失败!')
#
#
# print(sorted([36, 5, -12, 9, -21]))
# # 接受一个key函数来实现自定义的排序，例如，按数值的绝对值大小排序
# print(sorted([36, 5, -12, 9, -21], key=abs))
# # 字符串的排序，根据ASCII码来排序的
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# # 将上述函数进行反向排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#
# # 对下列的学生分数，按姓名排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def by_name(t):
#     # print('t = %s' % t[0])
#     return t[0]
#
#
# L2 = sorted(L, key=by_name)
# print(L2)
#
#
# # 按照成绩排序
# def by_score(t):
#     return t[1]
#
#
# L2 = sorted(L, key=by_score, reverse=True)
# print(L2)
#
#
#


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 延时计算求和
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# 调用lazy_sum()，返回的不是求和结果，而是求和函数：
f = lazy_sum(1,3,5,7,9)
print(f)

# 调用函数f时，才真正计算求和结果
print(f())

# 当我们调用函数lazy_sum()时，每次都会返回一个新的函数，即使传入的参数是一致的
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()

# 此处的打印结果都为9，与想要的结果不符
# 原因在于函数引用的i，并非立刻执行的。三个函数都返回时，引用的i变为3，因此最终结果为9
# 所以返回闭包时：返回函数不要引用任何循环变量，或者后续会发生变化的变量
print(f1())
print(f2())
print(f3())


# 此函数的正确写法应为
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

