#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/14

"""
    desc:pass
"""

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from dueros.LifeSkill.BotServer import application
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
