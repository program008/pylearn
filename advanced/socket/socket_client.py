#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
  Created by tao.liu on 2018/8/3.
  socket 客户端
"""
# 导入 socket、sys 模块
import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
