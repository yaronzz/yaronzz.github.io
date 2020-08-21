---
title: Macos初始配置与使用
urlname: macos_build
date: 2020-06-16 11:17:40
tags:
  - macos
categories:  
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/macos.jpg
thumbnail: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/macos.jpg
---

## 虚拟机配置  
1. 安装[VMware](https://www.vmware.com/cn.html) 

   版本15.5 序列号：

   ```tex
   UY758-0RXEQ-M81WP-8ZM7Z-Y3HDA
   VF750-4MX5Q-488DQ-9WZE9-ZY2D6
   UU54R-FVD91-488PP-7NNGC-ZFAX6
   YC74H-FGF92-081VZ-R5QNG-P6RY4
   YC34H-6WWDK-085MQ-JYPNX-NZRA2
   ```

2. 安装[VMware Unlocker](https://pan.baidu.com/s/19XFWF3aVIiYCHwL6Pq9yag)工具（提取码dagu），才能使用Macos

   下载完成后解压unlocker，将解压后的文件复制到Vmware的安装目录，使用管理员运行**unlocker.exe**和**win-install.cmd**。

   ![img](https://i.loli.net/2020/06/27/pL7CAhHrYaGImgN.png)

3. 安装[Macos10.15](https://pan.baidu.com/s/1gpmjn6vR1-UKOA67bFd3pg) 提取码 jlhr

4. 安装VMwareTool
<!--more-->

## 环境配置

1. **修改Host文件，解决GitHub的raw.githubusercontent.com无法连接问题** 

   打开终端输入`sudo vi /etc/hosts`,并复制黏贴以下内容，之后按ESC键，再输入`:wq`保存

   ```tex
   # GitHub Start
   52.74.223.119 github.com
   192.30.253.119 gist.github.com
   54.169.195.247 api.github.com
   185.199.111.153 assets-cdn.github.com
   151.101.76.133 raw.githubusercontent.com
   151.101.108.133 user-images.githubusercontent.com
   151.101.76.133 gist.githubusercontent.com
   151.101.76.133 cloud.githubusercontent.com
   151.101.76.133 camo.githubusercontent.com
   151.101.76.133 avatars0.githubusercontent.com
   151.101.76.133 avatars1.githubusercontent.com
   151.101.76.133 avatars2.githubusercontent.com
   151.101.76.133 avatars3.githubusercontent.com
   151.101.76.133 avatars4.githubusercontent.com
   151.101.76.133 avatars5.githubusercontent.com
   151.101.76.133 avatars6.githubusercontent.com
   151.101.76.133 avatars7.githubusercontent.com
   151.101.76.133 avatars8.githubusercontent.com
   # GitHub End
   ```

2. **安装brew** 

   打开终端，输入一下命令并按回车

   ```shell
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```

   可能会出现卡住的情况，如下：

   ```shell
   ==> Tapping homebrew/core
   Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core'...
   ```

   则直接按Ctrl+C退出，换源安装core，输入以下命令：

   ```shell
   cd /usr/local/Homebrew/Library/Taps/homebrew
   git clone git://mirrors.ustc.edu.cn/homebrew-core.git/ /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core --depth=1
   ```

   接下来修改为国内源，加速访问速度：

   ```shell
   cd /usr/local/homebrew
   git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
   cd /usr/local/homebrew/Library/Taps/homebrew/homebrew-core"
   git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
   cd /usr/local/homebrew/Library/Taps/homebrew/homebrew-cask"
   git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git
   /usr/local/homebrew/bin/brew update
   ```

   如果要换回原来的源，则输入以下命令：

   ```shell
   cd  /usr/local/homebrew
   git remote set-url origin https://github.com/homebrew/brew.git
   cd /usr/local/homebrew/Library/Taps/homebrew/homebrew-core
   git remote set-url origin https://github.com/homebrew/homebrew-core.git
   cd /usr/local/homebrew/Library/Taps/homebrew/homebrew-cask
   git remote set-url origin https://github.com/homebrew/homebrew-cask.git
   ```


## 软件安装
1. V2rayU

   地址：https://github.com/yanue/V2rayU/releases 

   功能：支持二维码扫描、URL导入等功能，跟V2rayN差不多

2. 谷歌浏览器 

   地址：https://www.google.com/intl/zh-CN/chrome/