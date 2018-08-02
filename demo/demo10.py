#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/8/2.
  面向对象
"""


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# 当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。例如:
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5


# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


# 类的方法
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
# 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = People('runoob', 10, 30)
p.speak()
# print("体重",p._weight) # AttributeError: 'People' object has no attribute '_weight'
