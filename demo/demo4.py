#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/7/31.
  python 循环语句
"""
n = 100
sum = 0
counter = 0

while counter <= n:
    sum += counter
    counter += 1

print("1到%d的和是%d" % (n, sum))

# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

# for语句
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
