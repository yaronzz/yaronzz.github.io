---
title: Charles抓包工具使用教程
urlname: charles_use
date: 2020-06-15 18:02:20
tags: 
  - charles
categories: 
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest//blog/charles.png
thumbnail: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest//blog/charles.png
---

[Charles](https://www.charlesproxy.com/)是一款抓包工具，能够在Windows，Mac，Linux上使用，个人觉得比Fiddler要好用得多。它可以提供代理服务，使手机或电脑软件通过它代理上网。

**注：**[破解教程](https://www.zzzmode.com/mytools/charles/)

<!-- more -->

### 使用教程

1. **安装电脑证书**

    选择菜单Help-->SSL Proxying-->Install Charles Root Certificate

    <img src="https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest//blog/charles1.png" alt="charles1" style="zoom: 80%;" />

2. **安装手机证书**

    选择菜单Help-->SSL Proxying-->Install Charles Root Certificate on a Mobile Device or Remote Browser

    ![charles2](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles2.png)

    手机与电脑连接同一个WIFI，进入WIFI设置，选择配置代理--手动，填写Charles提供的IP与端口

    <img src="https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charlesphone.jpg" alt="charlesphone" style="zoom: 50%;" />
    <img src="https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charlesphone1.jpg" alt="charlesphone1" style="zoom: 50%;" />

    手机使用浏览器登录网址 chls.pro/ssl ,下载并安装证书

3. **设置监听站点与数据**

    选择菜单Proxy-->SSL Proxying Settings，勾选Enable SSL Proxying，在Location部份选择add，按如下图添加，抓取任意站点、443端口的数据。

    ![charles3](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles3.png)

4. **设置代理**

    选择菜单Proxy-->Proxying Settings，勾选HTTP和SOCKS，填写自己的代理端口，如下所示。如果不需要代理这一步骤可以跳过。

    ![charles3](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles4.png)

    ![image-20200716155401866](https://i.loli.net/2020/07/16/WXKotBSPAglIOh5.png)

5. **开始抓包**

    选择菜单Proxy，勾选Windows Proxy，如果需要代理则再勾选External Proxy Settings

    ![image-20200716155638668](https://i.loli.net/2020/07/16/2KIwGsdkFVDeSxl.png)
    
    ![charles5](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles5.png)