---
title: Tidal-Media-Downloader Installation Documentation
urlname: tidal_dl_installation
date: 2020-03-16 16:10:33
tags: tidal
categories: 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/log.jpeg
top: True
thumbnail: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/log.jpeg
---

[**Tidal-Media-Downloader**](https://github.com/yaronzz/Tidal-Media-Downloader) is an application that lets you download videos、tracks、playlist、album and artist's album from [**Tidal Website**](https://listen.tidal.com/)

<!-- more -->

Have two version：

- **Tidal-dl**: cli，support windows\linux\macos\android
- **Tidal-gui**: gui，support windows

## 🎉Tidal-dl

<img src="https://i.loli.net/2020/08/19/gqW6zHI1SrKlomC.png" alt="image-20200819114623230" style="zoom: 80%;" />

### Install

Select the installation steps according to the computer system

- Windows：[tidal-dl.exe](https://github.com/yaronzz/Tidal-Media-Downloader/tree/master/TIDALDL-PY/exe)
- Linux: `pip3 install tidal-dl --upgrade`
- MacOs:

   ```
   brew instal ffmpeg
   brew install python
   curl -O http://python-distribute.org/distribute_setup.py
   python distribute_setup.py
   curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
   python get-pip.py
   pip3 install --upgrade tidal-dl
   tidal-dl
   ```

- Android: 

   a). Install termux：https://play.google.com/store/apps/details?id=com.termux
   b). Open permission：termux-setup-storage
   c). Install python和tidal-dl
   
   ```
   pkg install python clang libjpeg-turbo ffmpeg zlib -y
   apt update
   apt upgrade
   pkg update
   pip3 install --upgrade pip
   pip3 install --upgrade tidal-dl
   tidal-dl
   ```

### Use

1. Enter username and password.
2. Type '2' and enter，set config file

   | Name                           | Function                                          |
   | :----------------------------- | :------------------------------------------------ |
   | Download path                  | File save directory                               |
   | Audio quality                  | Track quality                                     |
   | Video quality                  | Support 1080\720\480\360\240                      |
   | Add hyphens                    | '-' between number and title, like‘01-Yellow.m4a’ |
   | Convert mp4 to m4a             | Convert mp4 to m4a(Only track)                    |
   | Add year                       | before or after the name of album directory       |
   | Add explicit tag               | like‘01-Yellow-explicit.m4a’                      |
   | Include singles                | download artist EP&Single                         |
   | Save covers                    | Cover-Files are saved in the album directory      |
   | Artist name before track-title | Add artist name before the track-file-name        |
   | ID before album-folder         | like '[20495848] Wretched and Divine'             |
   
   Audio quailty: Master > HiFi > High > Normal
   
   | Audio Quality    | Format             |
   | :--------------- | :----------------- |
   | Normal           | mp4 or m4a         |
   | High             | mp4 or m4a         |
   | HiFi             | mp4 or m4a or flac |
   | Master**(BEST)** | flac               |
   
3. Type track\video\album\playlist\artist url to download


## 🍕Tidal-gui

Because the gui more cumbersome to do, it is generally tidal-dl that adds new features first, and then gui follows up. Therefore it is recommended to use tidal-dl.

1. [Download Tidal-gui](https://github.com/yaronzz/Tidal-Media-Downloader/releases)
2. Open tidal-gui and set https-proxy and login

   <img src="https://i.loli.net/2020/08/21/KP1QcHjOnU63dgq.png" alt="image-20200821102515525" style="zoom:67%;" />

3. Type track\video\album\playlist\artist url to download

   <img src="https://i.loli.net/2020/08/06/sPLowIlCGyOdpVN.png" alt="2222" style="zoom:80%;" />


## 💎Disclaimer

- Music is not free, need a HIFI account.
- Private use only.
- Any secondary development of this tool has nothing to do with me.
- You should not use this method to distribute or pirate music.
- It may be illegal to use this in your country, so be informed.

## ⚽Q&A

1. **Does the tool require hi-fi account?**
   Yes.
2. **Can't download 'Master'?**
   Make sure the track or album you want to save has the "M" logo beside of it.
3. **Need gui for MacOs.**
   Need some times to learn swift.
4. **Requested quality is not allowed in user's subscription?**
   You need a hi-fi account.

