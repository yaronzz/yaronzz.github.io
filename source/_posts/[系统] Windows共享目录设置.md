---
title: Windows共享目录设置
urlname: windows_share
date: 2021-04-27 11:17:40
tags:
  - windows
categories:  
  - system
cover: 
---

局域网内文件分享时，共享功能是最方便的一个方式。

<!-- more -->

## 打开共享功能

1. 打开控制面板中的`网络和共享中心`

   ![image-20210427135616689](https://i.loli.net/2021/04/27/cPaCQD4GqorXjSs.png)

2. 选择`更改高级共享设置`

   ![image-20210427135702162](https://i.loli.net/2021/04/27/32nQ1orXj8saWgx.png)

3. 打开`所有网络`，配置设置如下图：

   ![image-20210427135752796](https://i.loli.net/2021/04/27/q6EXmbhdVk1Iso2.png)

## 修改安全选项

1. 按WIN+R，调出运行框

   ![img](https://i.loli.net/2021/04/27/4ZHDmfcAVbNkCrw.png)

2. 在运行框输入 gpedit.msc

   ![img](https://i.loli.net/2021/04/27/B8QJfZIqkR5UhVu.png)

3. 打开安全选项路径：`Windows设置 -- 安全设置 -- 本地策略 -- 安全选项`, 设置全部账户选项，如下图：

![image-20210427135119521](https://i.loli.net/2021/04/27/5mNz8i9VUFG4lvc.png)

