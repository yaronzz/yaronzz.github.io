---
title: Tidal-Media-Downloader安装文档
urlname: tidal_dl_installation_chn
date: 2020-03-16 15:51:31
tags: 
  - tidal
categories: 
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/log.jpeg
top: True
thumbnail: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/log.jpeg
---

[**Tidal-Media-Downloader**](https://github.com/yaronzz/Tidal-Media-Downloader)是一个从[Tidal音乐网站](https://listen.tidal.com/)下载音频资源的工具，支持下载歌曲、专辑、歌单、歌手全部专辑和批量下载功能。

<!-- more -->

目前有两个版本：

- **Tidal-dl**: 命令行模式，支持windows\linux\macos\android
- **Tidal-gui**: 界面模式，支持windows

## 🎉Tidal-dl

<img src="https://i.loli.net/2020/08/19/gqW6zHI1SrKlomC.png" alt="image-20200819114623230" style="zoom: 80%;" />

### 安装教程

根据电脑系统选择下面各自安装过程：

- Windows下安装：[tidal-dl.exe](https://github.com/yaronzz/Tidal-Media-Downloader/tree/master/TIDALDL-PY/exe)

- Linux下安装: `pip3 install tidal-dl --upgrade`
- MacOs下安装:

   ```shell
   brew instal ffmpeg
   brew install python
   curl -O http://python-distribute.org/distribute_setup.py
   python distribute_setup.py
   curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
   python get-pip.py
   pip3 install --upgrade tidal-dl
   tidal-dl
   ```

- Android下安装:

   a). 安装termux：https://play.google.com/store/apps/details?id=com.termux
   b). 打开权限：termux-setup-storage
   c). 安装python和tidal-dl

   ```shell
   pkg install python clang libjpeg-turbo ffmpeg zlib -y
   apt update
   apt upgrade
   pkg update
   pip3 install --upgrade pip
   pip3 install --upgrade tidal-dl
   tidal-dl
   ```

### 使用教程

1. 输入账号密码登录
2. 输入'2'回车，设置配置项

   | 名称                           | 功能                                              |
   | :----------------------------- | :------------------------------------------------ |
   | Download path                  | 输出目录                                          |
   | Convert mp4 to m4a             | 是否将Mp4格式的音频文件转换为M4a格式              |
   | Add explicit tag               | 是否在下载的歌曲文件名后加上explicit脏话标志      |
   | Add hyphens                    | 文件名的序号和歌名之间加扩折号，如‘01-Yellow.m4a’ |
   | Add user track number          | 文件名添加序号                                    |
   | Audio quality                  | 下载的音乐质量                                    |
   | Video quality                  | 下载的视频质量                                    |
   | Check exist                    | 跳过已经下载的文件                                |
   | Artist name before track-title | 歌曲文件名前歌手名称                              |
   | ID before album-folder         | 专辑文件夹名前加专辑ID                            |
   | Add year                       | 下载的专辑目录前或后加上发布年号                  |
   | Include singles                | 下载歌手专辑时，是否下载EP\单曲                   |
   | Save covers                    | 是否保存封面文件                                  |

   音频质量Audio quality的选择对应的文件格式如下：

   Master > HiFi > High > Normal

   | 音频质量 | 文件格式       |
   | :------- | :------------- |
   | Normal   | mp4或m4a       |
   | High     | mp4或m4a       |
   | HiFi     | flac或mp4或m4a |
   | Master   | flac           |

3. 输入链接或者ID即可下载


## 🍕Tidal-gui

因为界面做起来比较麻烦，所以一般都是tidal-dl先加新功能之后，gui再跟进。所有如果对界面需求不是很大的话，建议使用tidal-dl比较好。

1. [下载tidal-gui文件](https://github.com/yaronzz/Tidal-Media-Downloader-PRO/releases)
2. 打开tidal-gui设置https代理(不需要的可以不用)并登陆
   
   <img src="https://i.loli.net/2020/08/21/KP1QcHjOnU63dgq.png" alt="image-20200821102515525" style="zoom:67%;" />
   
3. 输入歌曲\专辑\视频\歌手ID或URL即可下载

   <img src="https://i.loli.net/2020/08/06/sPLowIlCGyOdpVN.png" alt="2222" style="zoom:80%;" />

## 💎免责声明

- 音乐不是免费的，需要开通HIFI会员。
- 这是一个私人工具，请不要用于商业和恶意传播等用途。
- 任何对此工具的二次开发，产生的后果跟本人无关。
- 请不要用此工具分发和盗版音乐。
- 在你的国家和地区使用此工具可能是违法的行为，请知悉。

## ⚽常见问题解答

1. **下载时，我是否需要开通会员？**
   答：当然
2. **为什么我下载的不是Master音质？**
   答：Tidal有些歌曲是没有到Master音质的，可以去网站上看看歌曲后面是否有M标志
3. **为什么没有MacOs的界面工具？**
   答：还不会Swift
4. **Requested quality is not allowed in user's subscription?**
   答：先检查自己是不是会员，另外有些歌曲在一些地区是限制下载的。

