#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/7/31.
  description this is description
"""
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

# 条件控制
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键退出")

sex = 0
if sex == 1:
    print("sex is man")
elif sex == 0:
    print("sex is woman")
else:
    print("sex not")
