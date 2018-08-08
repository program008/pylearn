#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
  Created by tao.liu on 2018/8/8.
  description this is description
"""
# python 字典类型转换为JSON对象
import json

data1 = {
    'no': 1,
    'name': 'ryan',
    'url': 'http://www.baidu.com'
}

json_str = json.dumps(data1)
print("python原始数据：" + repr(data1))
print("JSON对象：", json_str)

# 将JSON对象转换为Python字典
data2 = json.loads(json_str)
print("data2['name']", data2['name'])
print("data2['url']", data2['url'])
