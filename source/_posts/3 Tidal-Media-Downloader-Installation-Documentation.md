---
title: Tidal-Media-Downloader Installation Documentation
urlname: tidal_dl_installation
date: 2020-03-16 16:10:33
tags: 
  - tidal
categories: 
  - 软件
cover: https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/tidal_gui_login.jpg
top: True
---

[**Tidal-Media-Downloader**](https://github.com/yaronzz/Tidal-Media-Downloader) is an application that lets you download videos、tracks、playlist、album and artist's album from [**Tidal Website**](https://listen.tidal.com/)

Have two version：
- **Tidal-dl**: cli，support windows\linux\macos\android
- **Tidal-gui**: gui，support windows

## Tidal-dl Install&Use
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/tidal_dl_log.jpg)
### Install
First you need to install [**ffmpeg**](http://ffmpeg.org/) to download videos. Select the installation steps according to the computer system

**1. For Windows**：[tidal-dl.exe](https://github.com/yaronzz/Tidal-Media-Downloader/tree/master/TIDALDL-PY/exe)  
**2. For Linux**: ```pip3 install tidal-dl --upgrade```  
**3. For MacOs**:  
```
brew install python
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
pip3 install --upgrade tidal-dl
tidal-dl
```

**4. For Android**:  
a). Install termux：https://play.google.com/store/apps/details?id=com.termux  
b). Open permission：termux-setup-storage  
c). Install python和tidal-dl  
```
pkg install python clang libjpeg-turbo ffmpeg zlib -y
pip3 install --upgrade pip
pip3 install --upgrade tidal-dl
tidal-dl
```

### Use
1. Enter username and password.
2. Type '2' and enter，set config file

| 名称  | 功能   |
| --------- | ------ |
| Output directory  | File save directory |
| Sound Quality  | Track quality,support Low\High\Lossless\Hi_Res |
| Video Resolution  | Support 1080\720\480\360\240 |
| Download Threads  | Synchronous download,default '1' |
| Only M4a  | Convert mp4 to m4a(Only track) |
| Show download progress  | Enable when threadnum is 1 |
| Use hyphens  | '-' between number and title, like‘01-Yellow.m4a’ |
| Add year  | before or after the name of album directory |
| Add explicit tag | like‘01-Yellow-explicit.m4a’|
| Playlist songs in artist folders  | Organized with artist folder |
| Include singles  | download artist EP&Single |
| Save covers  | Cover-Files are saved in the album directory |

| Sound Quality  | Format   |
| --------- | ------ |
| LOW  | mp4 or m4a |
| HIGH  | mp4 or m4a |
| LOSSLESS  | flac |
| HI_RES  | flac |

1. Type track\video\album\playlist\artist url to download
2. Download by file
- [Download the example file](https://github.com/yaronzz/Tidal-Media-Downloader/blob/master/TIDALDL-PY/dllist-example.ini)
- Add the ID to the file
- Open tidal-dl，type the path of file

## Tidal-gui Install&Use

Because the gui more cumbersome to do, it is generally tidal-dl that adds new features first, and then gui follows up. Therefore  it is recommended to use tidal-dl.

1. [Download Tidal-gui](https://github.com/yaronzz/Tidal-Media-Downloader/releases)
2. Open tidal-gui and set https-proxy and login  
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/tidal_gui_login.jpg)

3. Open the button in the upper right corner of the gui and select settings. For configuration items, refer to the configuration of tidal-dl above.  
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/tidal_gui_settings.jpg)

4. Type track\album\video\artist id or url to download  
![image](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/tidal/tidal_gui_example.jpg)


## Disclaimer
- Musice is not free, need a hifi account.
- Private use only.
- Any secondary development of this tool has nothing to do with me.
- You should not use this method to distribute or pirate music.
- It may be illegal to use this in your country, so be informed.

## Q&A
1. **Does the tool require hi-fi account？**   
Yes.
2. **Can't download 'Master'？**  
Make sure the track or album you want to save has the "M" logo beside of it. 
3. **Need gui for MacOs.**  
Need some times to learn swift.
4. **Can's change threadnum on gui？**  
The thread-model has some bugs.
5. **Requested quality is not allowed in user's subscription?**  
You need a hi-fi account.
6. **Convert mp4 to m4a failed?**  
Install ffmpeg.

<!-- ## Donation
| Name  | Coffee  | Comment |
| --------- | ------ | ------ |
| Someone | 5 coffees |
| edgar | 3 coffees | Muchas Gracias |
| CaSa | 3 coffees | Great tool - thanks a lot :) |
| HellF | 1 coffee |
| Someone | 3 coffees | Happy Birthday |
| Someone | 3 coffee |
| IshimaruOficial | 3 coffees | I just wanted to thank you for the constant support of your tools, it's made my life at work so much better |
| burybury | 1 coffee |
| Someone | 2 coffee |
| Someone | 5 coffee | -->