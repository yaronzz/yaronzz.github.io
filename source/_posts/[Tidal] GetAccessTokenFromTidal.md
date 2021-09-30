---
title: Get AccessToken From Tidal
urlname: get_accesstoken
date: 2020-07-16 16:16:33
tags: [tidal]
categories: 
    - 软件
cover: https://i.loli.net/2020/07/16/lwV96j7QcYXqkaN.png
---



AccessToken is a key to get the track\video streamurl.

- AccessToken from Tidal Desktop: Support MQA Flac, can't download 360\Dobly
- AccessToken from Tidal Android: Support all
- AccessToken from Tidal IOS: Can't download Flac

<!-- more -->

How to use AccessToken.

- For tidal-dl: Open tidal-dl and Enter 10 to set AccessToken
- For tidal-gui: Open file tidal-ini and add a key "accesstoken=xxxxxxxxx" (xxxxxxx is your AccessToken)



## Get AccessToken from Tidal Android

1. Login Tidal Android and play a track
2. With any file explorer, go to /sdcard/Android/data/com.aspiro.tidal/cache/okhttp

   ![image-20200716170648460](https://i.loli.net/2020/07/16/Ihax72DuVU4wnZR.png)

3. Open a file in the folder and Find the 'Authorization: Bearer' **very_long_key** (At the beginning of the file)
   **very_long_key** is what you need to copy/paste, if the file not contain the 'Authorization: Bearer', open another file.

   ![image-20200716171249033](https://i.loli.net/2020/07/16/WRMmrUIHOBpizc1.png)

   

## Get AccessToken from Tidal Desktop

### Download Software

- [Tidal Desktop](https://offer.tidal.com/download?lang=en)
- [*Charles*](https://www.charlesproxy.com/download/) : View all of the HTTP and SSL / HTTPS traffic between their machine and the Internet

### Install Charles

1. Install Charles Root Certificate
   Select menu: Help --> SSL Proxying --> Install Charles Root Certificate

   <img src="https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest//blog/charles1.png" alt="charles1" style="zoom: 67%;" />

2. SSL Proxying Settings

   Select menu: Proxy-->SSL Proxying Settings

   Open SSL Proxying page and follow picture settings

   ![charles3](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles3.png)

3. Open Options

   - Windows Proxy
   - Start Recording
   - Start SSL Proxying
   
   ![image-20200716151604188](https://i.loli.net/2020/07/16/MU6zIPGOoe3KxBq.png)

4. External Proxy Settings (If you need VPN to use Tidal Desktop)

   Select menu: Proxy-->Proxying Settings

   Open Proxies page \ Windows page and follow picture settings

   ![charles3](https://cdn.jsdelivr.net/gh/yaronzz/CDN@latest/blog/charles4.png)

   ![image-20200716155401866](https://i.loli.net/2020/07/16/WXKotBSPAglIOh5.png)

   Select menu: Proxy-->External Proxying Settings

   Follow picture settings (IP and Port come from your VPN)

   ![image-20200716155638668](https://i.loli.net/2020/07/16/2KIwGsdkFVDeSxl.png)

### Get AccessToken

1. Install Charles and Open it 
2. Open Tidal Desktop

   Charles will view all of the HTTP / HTTPS traffic between tidal and the Internet.

   ![image-20200716152531935](https://i.loli.net/2020/07/16/WzHRUks6TLvuflO.png)

3. Relogin on the Tidal Desktop and play a track 

   ![image-20200716155903395](https://i.loli.net/2020/07/16/lwV96j7QcYXqkaN.png)

4. 'Ctrl + F' on the Charles

   - Enter 'authorization: Bearer' or 'authorization' and click Find-Button

   - Select url contains 'tidal'

   - Double click the selection

     ![image-20200716161326262](https://i.loli.net/2020/07/16/PfL7GX1oZrAVkiv.png)

   - Select Contents page copy the authorization (remove 'Bearer ')

     ![image-20200716161139356](https://i.loli.net/2020/07/16/2CFoVeZ6DxHrb18.png)


## Q&A

   1. Follow documentation but I can't get the AccessToken'
      Google how to use Charles.
   2. How to get AccessToken from Tidal IOS
      Google Charles IOS.

