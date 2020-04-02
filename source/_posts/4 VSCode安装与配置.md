---
title: VSCode安装与配置 
urlname: vscode_install
date: 2020-03-16 11:33:56
tags: 
  - vscode
categories:  
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN/blog/vscode.jpg
---

Visual Studio Code是由微软研发的一款免费、开源的跨平台代码编辑器。其提供的插件包罗万象，可以说是目前市面上最优秀的一款编辑器。
- 官网地址：https://code.visualstudio.com/
- Github地址：https://github.com/Microsoft/vscode

### 配置
- 自动换行：文件->首选项->设置->直接搜索 -> Editor:WordWrap,将off修改为on即可
- 用户代码片段：打开vscode>文件>首选项>用户代码片段

### 必转扩展
- 汉化：Chinese (Simplified) Language Pack
- 主题：Atom One Dark Theme
- 图标：Material Icon Theme
- MD文件：Markdown All in One
- 对齐：Better Align
- 括号颜色：Bracket Pair Colorizer
- 对齐辅助线：Guides
- 多设备同步：Settings Sync
- TODO高亮：TODO Highlight


### Settings Sync配置
主要用于同步软件配置，包括代码段、主题、插件、图标等，只需要在一台电脑上配好，其他电脑就能直接下载同步，省了一堆麻烦.

**github操作**
1. 进入github/Settings/Developer settings/Personal access tokens,点击Generate New Token新建一个token
2. 描述填写vscode同步，gist打钩
3. 复制新建成功后提供的Access Token

**vscode操作**
1. 按F1，输入Sync:Update/Upload Settings
2. 输入Access Token，创建gists，进行配置上传
3. 上传成功后，会返回一个Gist ID，保存该Gist ID，下次其他设备需要下载配置时需要用到

