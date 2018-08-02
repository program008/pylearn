#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/8/2.
  类属性和方法
"""

# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时
# self.__private_attrs。
#
# 类的方法
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，
# self 代表的是类的实例。
#
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
#
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。
# self.__private_methods。
from dataclasses import dataclass


class JustCounter:
    __secretCount = 0  # 私有变量
    _name = "这不是私有的变量"
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
counter.count()
print(counter._name)
print(counter.publicCount)


# print(counter.__secretCount)  # 报错，实例不能访问私有变量

class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    @staticmethod
    def __foo():  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出


# x.__foo()  # 报错

# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 运算符重载
# Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)


a = people('孙悟空', 999)
print(a)


# 最新的 Python3.7 中(2018.07.13)，对类的构造函数进行了精简
@dataclass
class A:
    x: int
    y: int

    def add(self):
        return self.x + self.y


class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


class C:
    def __init__(self, name):
        self.name = name

    def println(self):
        print(self.name)


c = C("我是Ryan")
c.println()
