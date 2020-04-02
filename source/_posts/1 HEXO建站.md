---
title: HEXO建站
urlname: hexo_build
date: 2020-03-11 10:47:20
tags: 
  - hexo
  - 教程
categories: 
  - 建站
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN/blog/hexo.jpg
---
### 一、github准备
- 在github新建项目'xxxx.github.io'，其中xxxx为账号名，克隆项目到本地
- 配置ssh
1. 生成秘钥：ssh-keygen -t rsa -C "你的邮件地址"
2. 复制公钥文件内容，默认为id_rsa.pub
3. 登录Github，点击头像->Settings—>SSH keys—>Add SSH key
4. 把公钥粘贴到key中，填好title并点击Add key
5. 输入命令'ssh -T git@github.com'，选yes，等待片刻可看到成功提示


### 二、环境准备
- 安装node.js： https://nodejs.org/en/download/
- 安装hexo：
```
npm config set registry http://registry.npm.taobao.org //设置国内镜像链接
npm install hexo-cli -g
npm install hexo --save
```

### 三、新建博客
- 在github克隆下来的文件夹中建站
```
hexo init #初始化博客
hexo g   #编译成静态网页
hexo s   #本地测试
```

- 新建文章
```
hexo new "test"
```

- 新建标签页和分类页
1. 输入命令
```
hexo new page tags
hexo new page categories
```
2. 打开生成的文件'source/tags/index.md'和'source/categories/index.md'
3. 分别添加 type: "tags" 和 type: "categories"


### 四、部署
- 输入命令 'npm install hexo-deployer-git --save'
- 打开根目录下'_config.yml',添加内容
```
deploy:
  type: git
  repo: git@github.com:your_name/your_name.github.io.git
  branch: master
```
- 执行编译上传命令
```
hexo d -g
```

### 五、域名绑定
- 域名解析
1. 添加一个CNAME记录，主机记录@，记录值xxx.github.io，其他默认
1. 添加一个CNAME记录，主机记录www，记录值xxx.github.io，其他默认

- github设置
1. 打开项目'xxxx.github.io'，选择settings页面
2. 找到Custom domain，填写域名，不用加www
3. Enforce HTTPS打钩
4. 在博客根目录source下新建CNAME文件，填写域名