---
title: Linux挂载OneDrive
urlname: linux_mount_onedrive
date: 2020-08-15 08:57:02
tags: 
	- linux
	- onedrive
categories: 软件
cover: https://i.loli.net/2020/08/15/SkOXh1jHxsAf4le.jpg
---

### 🎉获取授权码

1. 下载Windows版本[rclone](https://rclone.org/downloads/)并解压。

2. 在目录下运行命令 `rclone authorize "onedrive"`

3. 复制授权码：`{"access_token":"xxxx"}`

   ![image-20200815092021152](https://i.loli.net/2020/08/15/4p2tTQ8yJ7RsxHO.png)

### 🎁安装rclone

1. 安装rclone

   ```shell
   curl https://rclone.org/install.sh | sudo bash
   ```

2. 配置

   ```shell
   rclone config
   ```

   设置步骤如下：
   
   ```shell
   root@localhost:~# rclone config
   No remotes found - make a new one
   n) New remote
   s) Set configuration password
   q) Quit config
   n/s/q> n  #新建一个挂载
   name> myone  #设置挂载的名称myone
   Type of storage to configure.
   Enter a string value. Press Enter for the default ("").
   Choose a number from below, or type in your own value
    1 / 1Fichier
      \ "fichier"
    2 / Alias for an existing remote
      \ "alias"
    3 / Amazon Drive
      \ "amazon cloud drive"
    4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
      \ "s3"
    5 / Backblaze B2
      \ "b2"
    6 / Box
      \ "box"
    7 / Cache a remote
      \ "cache"
    8 / Citrix Sharefile
      \ "sharefile"
    9 / Dropbox
      \ "dropbox"
   10 / Encrypt/Decrypt a remote
      \ "crypt"
   11 / FTP Connection
      \ "ftp"
   12 / Google Cloud Storage (this is not Google Drive)
      \ "google cloud storage"
   13 / Google Drive
      \ "drive"
   14 / Google Photos
      \ "google photos"
   15 / Hubic
      \ "hubic"
   16 / In memory object storage system.
      \ "memory"
   17 / Jottacloud
      \ "jottacloud"
   18 / Koofr
      \ "koofr"
   19 / Local Disk
      \ "local"
   20 / Mail.ru Cloud
      \ "mailru"
   21 / Mega
      \ "mega"
   22 / Microsoft Azure Blob Storage
      \ "azureblob"
   23 / Microsoft OneDrive
      \ "onedrive"
   24 / OpenDrive
      \ "opendrive"
   25 / OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
      \ "swift"
   26 / Pcloud
      \ "pcloud"
   27 / Put.io
      \ "putio"
   28 / QingCloud Object Storage
      \ "qingstor"
   29 / SSH/SFTP Connection
      \ "sftp"
   30 / Sugarsync
      \ "sugarsync"
   31 / Tardigrade Decentralized Cloud Storage
      \ "tardigrade"
   32 / Transparently chunk/split large files
      \ "chunker"
   33 / Union merges the contents of several upstream fs
      \ "union"
   34 / Webdav
      \ "webdav"
   35 / Yandex Disk
      \ "yandex"
   36 / http Connection
      \ "http"
   37 / premiumize.me
      \ "premiumizeme"
   38 / seafile
      \ "seafile"
   Storage> 23  #选择第23项的onedrive
   ** See help for onedrive backend at: https://rclone.org/onedrive/ **
   
   Microsoft App Client Id
   Leave blank normally.
   Enter a string value. Press Enter for the default ("").
   client_id>   #跳过
   Microsoft App Client Secret
   Leave blank normally.
   Enter a string value. Press Enter for the default ("").
   client_secret>  #跳过
   Edit advanced config? (y/n)
   y) Yes
   n) No (default)
   y/n>  #跳过
   Remote config
   Use auto config?
    * Say Y if not sure
    * Say N if you are working on a remote or headless machine
   y) Yes (default)
   n) No
   y/n> n  #选择n
   For this to work, you will need rclone available on a machine that has
   a web browser available.
   
   For more help and alternate methods see: https://rclone.org/remote_setup/
   
   Execute the following on the machine with the web browser (same rclone
   version recommended):
   
           rclone authorize "onedrive"
   
   Then paste the result below:
   result> {"access_token":"xxxxxxxx"}  #输入授权码
   Choose a number from below, or type in an existing value
    1 / OneDrive Personal or Business
      \ "onedrive"
    2 / Root Sharepoint site
      \ "sharepoint"
    3 / Type in driveID
      \ "driveid"
    4 / Type in SiteID
      \ "siteid"
    5 / Search a Sharepoint site
      \ "search"
   Your choice> 1   #选择1，onedrive
   Found 1 drives, please select the one you want to use:
   0:  (personal) id=xxxxxxxx
   Chose drive to use:> 0  #选择挂载的onedrive网盘
   Found drive 'root' of type 'personal', URL: https://onedrive.live.com/?cid=xxxxxxxx
   Is that okay?
   y) Yes (default)
   n) No
   y/n>  #跳过
   --------------------
   [myone]
   type = onedrive
   token = {"access_token":"xxxxxxxx"}
   drive_id = xxxxxx
   drive_type = personal
   --------------------
   y) Yes this is OK (default)
   e) Edit this remote
   d) Delete this remote
   y/e/d> y  #跳过
   Current remotes:
   
   Name                 Type
   ====                 ====
   myone                onedrive
   
   e) Edit existing remote
   n) New remote
   d) Delete remote
   r) Rename remote
   c) Copy remote
   s) Set configuration password
   q) Quit config
   e/n/d/r/c/s/q> 
   ```

### 🎨挂载

1. 新建Linux下的文件夹

   ```shell
   rm -rf /root/music  #删除已有的目录
   mkdir /root/music  #新建目录
   ```
   
2. 挂载磁盘

   ```shell
   rclone mount myone:音乐 /root/music --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000
   ```

   挂载成功后，输入`df -h`命令查看

   ![image-20200815181741080](https://i.loli.net/2020/08/15/y2B5TYqenzbkDcX.png)

3. 卸载磁盘

   ```shell
   fusermount -qzu LocalFolder
   ```

### 👔设置开机启动

1. 新建服务文件

   ```shell
   vim /etc/systemd/system/rclone.service
   ```

   往文件中输入以下内容：

   ```ini
   [Unit]
   Description=Rclone
   After=network-online.target
   
   [Service]
   Type=simple
   ExecStart=/usr/bin/rclone mount myone:音乐 /root/music --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000
   Restart=on-abort
   User=root
   
   [Install]
   WantedBy=default.target
   ```

2. 启停服务

   ```shell
   #启动
   systemctl start rclone
   #暂停
   systemctl stop rclone
   #开机启动
   systemctl enable rclone
   ```

   





