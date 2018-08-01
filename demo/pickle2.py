#!/usr/bin/env python3
"""
  Created by tao.liu on 2018/8/1.
  description this is description
"""
#使用pickle模块从文件中重构python对象
import pickle
import pprint

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()