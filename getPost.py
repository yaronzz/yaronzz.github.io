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

src = "G:/OneDrive/写作/笔记/"
desc = "G:/code/myblog/source/_posts/"
ext = ".md"

files = pathHelper.getDirFiles(desc)
for item in files:
    pathHelper.remove(item)

files = pathHelper.getDirFiles(src)
for item in files:
    name = pathHelper.getFileName(item)
    to = desc + name
    pathHelper.copyFile(item, to)
    print(item)
