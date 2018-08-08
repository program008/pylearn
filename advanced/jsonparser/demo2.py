#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
  Created by tao.liu on 2018/8/8.
  description this is description
"""

import json

# data = {
#     'no': 1,
#     'name': 'ryan',
#     'url': 'http://www.baidu.com'
# }
# 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
