---
title: VSCode安装与配置 
urlname: vscode_install
date: 2020-03-16 11:33:56
tags: 
  - vscode
categories:  
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN/blog/vscode1.jpg
thumbnail: https://cdn.jsdelivr.net/gh/yaronzz/CDN/blog/vscode1.jpg
---

[Visual Studio Code](https://code.visualstudio.com/)是由微软研发的一款免费、跨平台代码编辑器。其提供的插件包罗万象，可以说是目前市面上最优秀的一款编辑器，软件在[Github](https://github.com/Microsoft/vscode)上提供开源代码。
<!-- more -->

## 🍕配置
- 自动换行：文件 -> 首选项 -> 设置 -> 直接搜索 -> Editor:WordWrap，将off修改为on即可

- 用户代码片段：打开vscode ->文件  ->首选项 ->用户代码片段


## 🍔必装扩展
1. 汉化：Chinese (Simplified) Language Pack

2. 主题：Atom One Dark Theme

3. 图标：Material Icon Theme

4. MD文件：Markdown All in One

5. 对齐：Better Align

6. 括号颜色：Bracket Pair Colorizer

7. 对齐辅助线：Guides

8. 多设备同步：Settings Sync

9. TODO高亮：TODO Highlight


## 🍟相关问题

### ✅Python no module的解决方法

调试python时，工作目录为当前文件所在目录，所以会导致文件找不到，no module等问题，需要在`launch.json`文件中添加`evn`参数：`"env": {"PYTHONPATH":"${workspaceRoot}"}`，完整配置如下：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceRoot}"
            },
        }
    ]
}
```

