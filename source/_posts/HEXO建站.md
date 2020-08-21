---
title: HEXO建站
urlname: hexo_build
date: 2020-03-11 10:47:20
tags: [hexo,教程]
categories: 建站
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN/blog/hexo.jpg
toc: true
---



## 🎉环境安装

- 安装 [node.js](https://nodejs.org/en/download/)

- 安装 HEXO

  ```shell
  npm config set registry http://registry.npm.taobao.org //设置国内镜像链接
  npm install hexo-cli -g
  npm install hexo --save
  npm install hexo-deployer-git --save
  ```

## 🎨新建博客

- 新建博客文件夹，在目录下输入以下命令：

  ```shell
  hexo init #初始化博客
  hexo g   #编译成静态网页
  hexo s   #本地测试
  ```

- 新建文章

  ```shell
  hexo new "测试文章"
  ```

- 新建页面

  ```shell
  hexo new page tags  #标签页
  hexo new page categories  #归档页
  ```

  打开生成的文件`source/tags/index.md`和`source/categories/index.md`，分别添加 `type: "tags"` 和 `type: "categories"`。

- 生成博客，并在本地部署

  ```
  hexo g
  hexo s
  ```

  浏览器打开 `127.0.0.1:4000` 即可浏览博客

## 🍕部署到Github

1. 在github新建项目[xxxx.github.io](http://xxxx.github.io/)，其中xxxx为账号名，克隆项目到本地

2. 配置ssh

   - 生成秘钥：`ssh-keygen -t rsa -C "你的邮件地址"`
   - 复制公钥文件内容，默认为id_rsa.pub
   - 登录Github，点击头像 -> Settings -> SSH keys -> Add SSH key
   - 把公钥粘贴到key中，填好title并点击Add key
   - 输入命令`ssh -T git@github.com`，选yes，等待片刻可看到成功提示

3. 打开博客目录下的`_config.yml`，在文件中添加：

   ```yaml
   deploy:
       type: git
       repo: git@github.com:your_name/your_name.github.io.git
       branch: master
   ```

4. 执行编译上传命令 `hexo d -g`，浏览器打开 `xxxx.github.io` 即可浏览博客

5. 域名解析

   - 添加一个CNAME记录，主机记录@，[记录值xxx.github.io](http://xn--xxx-2w0e630et04d.github.io/)，其他默认
   - 添加一个CNAME记录，主机记录www，[记录值xxx.github.io](http://xn--xxx-2w0e630et04d.github.io/)，其他默认

6. github设置
   - 打开项目'[xxxx.github.io](http://xxxx.github.io/)'，选择settings页面
   - 找到Custom domain，填写域名，不用加www
   - Enforce HTTPS打钩
   - 在博客根目录source下新建CNAME文件，填写域名