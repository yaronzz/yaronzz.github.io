---
title: Office365家庭版却需要激活专业增强版的解决办法 
urlname: office365
date: 2020-06-26 15:00:33
tags: 
    - office
categories: 
    - 软件
cover: https://i.loli.net/2020/06/28/Cye7miMJtL9fExU.jpg
---

由于之前使用KMS破解过office，所以安装了正版的office365家庭版之后，打开却显示当前版本是专业增强版，并且需要许可证。

<!-- more -->

<img src="https://i.loli.net/2020/06/26/H8pUtY6SxTqszQ4.png" alt="IMG" style="zoom:67%;" />

## 解决方法
1. 以**管理员**身份运行CMD
2. 输入命令切换到office目录 ```cd C:\Program Files\Microsoft Office\Office16```
3. 输入命令查询破解软件的KEY(位) ```cscript ospp.vbs /dstatus```
4. 输入命令卸载KEY ```cscript ospp.vbs /unpkey:XXXXX```

<img src="https://i.loli.net/2020/06/26/FyX3YQ5KoGfzbPx.png" alt="IMG" style="zoom:67%;" />

