#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/8/1.
  模块
"""
import sys

from demo import fibo

print('命令行参数如下:')
for i in sys.argv:
    print(i)

# print('\n\nPython 路径为：', sys.path, '\n')

fibo.fib(1000)
fibo.fib2(100)

fibo.__name__

