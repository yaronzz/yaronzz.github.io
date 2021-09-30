#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   getPost.py
@Time    :   2020/08/15
@Author  :   Yaronzz
@Version :   1.0
@Contact :   yaronhuang@foxmail.com
@Desc    :   
'''
import aigpy.pathHelper as pathHelper

src = "E:/OneDrive/写作/笔记/"
desc = "./source/_posts/"
ext = ".md"

files = pathHelper.getFiles(desc)
for item in files:
    pathHelper.remove(item)

files = pathHelper.getFiles(src)
for item in files:
    name = pathHelper.getFileName(item)
    to = desc + name
    pathHelper.copyFile(item, to)
    print(item)
