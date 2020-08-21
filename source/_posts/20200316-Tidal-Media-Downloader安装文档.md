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

目前有两个版本：

- **Tidal-dl**: 命令行模式，支持windows\linux\macos\android
- **Tidal-gui**: 界面模式，支持windows

## 一、Tidal-dl

<img src="https://i.loli.net/2020/06/28/k2uXqS4VeHG3R1n.png" alt="image" style="zoom:67%;" />

### 安装教程

因为下载视频时有合并和转换的步骤，所以需要先安装[**ffmpeg**](http://ffmpeg.org/)，接下来根据电脑系统选择下面各自安装过程。

1. Windows下安装：[tidal-dl.exe](https://github.com/yaronzz/Tidal-Media-Downloader/tree/master/TIDALDL-PY/exe)

2. Linux下安装: `pip3 install tidal-dl --upgrade`

3. MacOs下安装:

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

4. Android下安装:

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

   | 名称                             | 功能                                              |
   | :------------------------------- | :------------------------------------------------ |
   | Output directory                 | 输出目录                                          |
   | Sound Quality                    | 下载的音乐质量                                    |
   | Video Resolution                 | 下载的视频质量                                    |
   | Download Threads                 | 下载的线程数，一般设置为1                         |
   | Only M4a                         | 是否将Mp4格式的音频文件转换为M4a格式              |
   | Show download progress           | 是否显示进度条(只有当线程数为1时有效)             |
   | Use hyphens                      | 文件名的序号和歌名之间加扩折号，如‘01-Yellow.m4a’ |
   | Add year                         | 下载的专辑目录前或后加上发布年号                  |
   | Add explicit tag                 | 是否在下载的歌曲文件名后加上explicit脏话标志      |
   | Playlist songs in artist folders | 将歌单每首歌下载到以歌手为划分的目录下            |
   | Include singles                  | 下载歌手专辑时，是否下载EP\单曲                   |
   | Save covers                      | 是否保存封面文件                                  |
| ArtistName Before Track-Title    | 歌曲文件名前歌手名称                              |
   | Add ID Before AlbumFolderName    | 专辑文件夹名前加专辑ID                            |

   音频质量Sound Quality的选择对应的文件格式如下：
   
   HI_RES > LOSSLESS > HIGH > LOW
   
   | 音频质量 | 文件格式       |
   | :------- | :------------- |
   | LOW      | mp4或m4a       |
   | HIGH     | mp4或m4a       |
   | LOSSLESS | flac或mp4或m4a |
   | HI_RES   | flac           |

3. 输入歌曲\视频\专辑\歌单\歌手的链接即可下载

4. 批量下载

   - [下载样例文件](https://github.com/yaronzz/Tidal-Media-Downloader/blob/master/TIDALDL-PY/dllist-example.ini) 

   - 往文件中添加要下载的ID

   - 打来tidal-dl，输入样例文件地址

## 二、Tidal-gui

因为界面做起来比较麻烦，所以一般都是tidal-dl先加新功能之后，gui再跟进。所有如果对界面需求不是很大的话，建议使用tidal-dl比较好。

1. [下载tidal-gui文件](https://github.com/yaronzz/Tidal-Media-Downloader/releases)

2. 打开tidal-gui设置https代理(不需要的可以不用)并登陆
   
   <img src="https://i.loli.net/2020/06/28/hElSwsWmuXjPCFa.png" alt="Snipaste_2020-07-08_02-20-49.png" style="zoom:80%;" />
   
3. 输入歌曲\专辑\视频\歌手ID或URL即可下载

   <img src="https://i.loli.net/2020/06/28/zKMktEwX6aWySLN.png" alt="2222" style="zoom:80%;" />

## 三、免责声明

- 音乐不是免费的，需要开通HIFI会员。
- 这是一个私人工具，请不要用于商业和恶意传播等用途。
- 任何对此工具的二次开发，产生的后果跟本人无关。
- 请不要用此工具分发和盗版音乐。
- 在你的国家和地区使用此工具可能是违法的行为，请知悉。

## 四、常见问题解答

1. **下载时，我是否需要开通会员？**
   
   答：当然
   
2. **为什么我下载的不是Master音质？**

   答：Tidal有些歌曲是没有到Master音质的，可以去网站上看看歌曲后面是否有M标志

3. **为什么没有MacOs的界面工具？**

   答：还不会Swift

4. **为什么GUI的线程数不能改**

   答：最多只支持两条线程同时工作，不过多线程模块有点BUG，等有空再改

5. **Requested quality is not allowed in user's subscription?**

   答：先检查自己是不是会员，另外有些歌曲在一些地区是限制下载的。

6. **GUI怎么设置代理？**

   答：gui在登陆界面的右上角就可以设置

7. **mp4格式没有转换为m4a?**

   答：安装ffmpeg

