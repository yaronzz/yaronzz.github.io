---
title: jsDelivr加速Github图床
urlname: jsdelivr_cdn_github
date: 2020-03-29 11:16:03
tags:
  - jsdelivr
  - github
categories:  
  - 建站
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/github_cdn/jsDelivr.jpg
---

写博客经常会遇到的问题就是图片的存放，既要保证图片存放地址的稳定，也要保证图片访问的速度。在网上找了许多方法，其中最简单的就是直接使用专门的图床网站，比如[sm.ms](https://sm.ms/)之类。但总感觉不是太好整理，另外以后要搬运或者版本更新也不是很方便，于是想到了以[Github](https://github.com/)作为图床，再用[jsDelivr](https://www.jsdelivr.com/)来加速访问。

# jsDelivr加速访问
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/github_cdn/jsDelivr.jpg)  
jsDelivr是一家免费的公共的CDN服务器提供商，由于Github在国内的访问速度很慢，而且时不时断线，所以推荐使用jsDelivr作为CDN加速。只需要将文件的访问链接简单改一下即可，格式如下：
```
https://cdn.jsdelivr.net/gh/用户名/仓库名@latest/图片的路径/图片名称.jpg
```


# Github图床
GitHub是一个面向开源及私有软件项目的托管平台，也是目前世界最大的程序员集中地。除了用来当做程序的版本控制库之外，也可以储存其他的东西，Github图床主要也是图个稳定，只要不恶意刷流量影响也就不大。

## 1. 新建Github仓库
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/github_cdn/newrepo.jpg) 
- 仓库名随意
- 权限选择公开
- 使用Readme.md初始化

## 2. 生成仓库的访问钥匙token
- 右上角点击头像，选择Settings
- 选择Developer settings/Personal access tokens
- 点击Generate new token，获取token并复制下来  
- Note名称随便填，repo需要打钩，其他不用管
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/github_cdn/tokencreat.jpg) 

## 3. 下载配置PicGo
- 选择相应的电脑版本下载: https://github.com/Molunerfinn/PicGo/releases
- 配置图床信息：
```
仓库名：github用户名/仓库门
分支名：填master
存储路径：仓库中的目录名
自定义域名：https://cdn.jsdelivr.net/gh/用户名/仓库名@latest/
```
1. 下载图片上传软件[PicGo](https://github.com/Molunerfinn/PicGo/releases)，设置刚才新建的repo名称、token、分支名写master，存储地址填写本地图片存放目录。
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/github_cdn/picgoset.jpg) 



