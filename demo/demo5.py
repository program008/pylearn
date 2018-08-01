#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/7/31.
  迭代器和生成器
"""
import sys

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

list = [1, 2, 3, 4, 5]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
