---
title: Rclone使用教程 - 挂载Onedrive和谷歌网盘
urlname: rclone_use
date: 2020-08-15 08:57:02
tags: 
	- linux
	- onedrive
	- rclone
	- googledrive
categories: 软件
cover: https://i.loli.net/2020/08/15/SkOXh1jHxsAf4le.jpg
---

Rclone 是一个用于多个云平台之间同步文件和目录的命令行工具，其支持多种运营商网盘。

- 官网网址：[https://rclone.org](https://www.moewah.com/go/aHR0cHM6Ly9yY2xvbmUub3Jn)
- 开源地址：https://github.com/ncw/rclone

<!-- more -->

## 安装与配置

### 下载安装rclone

1. windows版本：下载[rclone](https://rclone.org/downloads/)并解压

2. Linux版本：

   ```shell
   curl https://rclone.org/install.sh | sudo bash
   ```

### 配置OneDrive

1. 在目录下打开cmd运行命令 `rclone authorize "onedrive"`

   世纪互联运行的命令 `rclone authorize onedrive "应用程序(客户端)ID" "客户端密码值" --onedrive-is-21vianet-version=true`

2. 复制授权码：`{"access_token":"xxxx"}`

   ![image-20200815092021152](https://i.loli.net/2020/08/15/4p2tTQ8yJ7RsxHO.png)

3. 配置

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
   name> onedrive  #设置挂载的名称onedrive
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
   onedrive                onedrive
   
   e) Edit existing remote
   n) New remote
   d) Delete remote
   r) Rename remote
   c) Copy remote
   s) Set configuration password
   q) Quit config
   e/n/d/r/c/s/q> 
   ```

### 配置谷歌网盘

运行命令：

```shell
rclone config
```

设置步骤如下：

```shell
$ ./rclone.exe config
Current remotes:

Name                 Type
====                 ====
onedrive             onedrive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> n #新建
name> gdrive  #名称
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS,
 Minio, etc)
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
Storage>     13  #第13选谷歌网盘
** See help for drive backend at: https://rclone.org/drive/ **

Google Application Client Id
Setting your own is recommended.
See https://rclone.org/drive/#making-your-own-client-id for how to create your own.
If you leave this blank, it will use an internal key which is low performance.
Enter a string value. Press Enter for the default ("").
client_id>
Google Application Client Secret
Setting your own is recommended.
Enter a string value. Press Enter for the default ("").
client_secret>
Scope that rclone should use when requesting access from drive.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Full access all files, excluding Application Data Folder.
   \ "drive"
 2 / Read-only access to file metadata and file contents.
   \ "drive.readonly"
   / Access to files created by rclone only.
 3 | These are visible in the drive website.
   | File authorization is revoked when the user deauthorizes the app.
   \ "drive.file"
   / Allows read and write access to the Application Data folder.
 4 | This is not visible in the drive website.
   \ "drive.appfolder"
   / Allows read-only access to file metadata but
 5 | does not allow any access to read or download file content.
   \ "drive.metadata.readonly"
scope>     1  #输入1赋予访问权限
ID of the root folder
Leave blank normally.

Fill in to access "Computers" folders (see docs), or for rclone to use
a non root folder as its starting point.

Enter a string value. Press Enter for the default ("").
root_folder_id>
Service Account Credentials JSON file path 
Leave blank normally.
Needed only if you want use SA instead of interactive login.
Enter a string value. Press Enter for the default ("").
service_account_file>
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n>   #跳过
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes (default)
n) No
y/n>  #跳过
```

### 获取配置文件

搜索 ，windows下正常都在 `C:\Users\你的用户名\\.config\rclone`目录下，Linux正常都在 `./.config/rclone/`目录下

## 使用教程

常用命令：

```shell
rclone config - 以控制会话的形式添加rclone的配置，配置保存在.rclone.conf文件中。
rclone copy - 将文件从源复制到目的地址，跳过已复制完成的。
rclone sync - 将源数据同步到目的地址，只更新目的地址的数据。
rclone move - 将源数据移动到目的地址。
rclone delete - 删除指定路径下的文件内容。
rclone purge - 清空指定路径下所有文件数据。
rclone mkdir - 创建一个新目录。
rclone rmdir - 删除空目录。
rclone check - 检查源和目的地址数据是否匹配。
rclone ls - 列出指定路径下所有的文件以及文件大小和路径。
rclone lsd - 列出指定路径下所有的目录/容器/桶。
rclone lsl - 列出指定路径下所有文件以及修改时间、文件大小和路径。
rclone md5sum - 为指定路径下的所有文件产生一个md5sum文件。
rclone sha1sum - 为指定路径下的所有文件产生一个sha1sum文件。
rclone size - 获取指定路径下，文件内容的总大小。.
rclone version - 查看当前版本。
rclone cleanup - 清空remote。
rclone dedupe - 交互式查找重复文件，进行删除/重命名操作。
```

1. 显示网盘上的目录

   ```shell
   rclone lsd onedrive:   #onedrive是上面设置的名称
   rclone lsd gdrive:    #gdrive是上面设置的名称
   ```

2. 拷贝谷歌网盘上的文件到Onedrive

   ```shell
   !rclone copy gdrive:music onedrive:音乐 --ignore-existing --config ./music/rclone.conf 
   # --config xxxx.conf 表示指定配置文件
   # --ignore-existing表示跳过已存在的文件
   # 此命令表示将谷歌网盘下的music目录复制到Onedrive网盘下的音乐目录
   ```

3. 挂在Onedrive

   ```shell
   rclone mount onedrive:音乐 music --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000 --config /content/gdrive/My\ Drive/music/rclone.conf
   ```

   

## Linux上挂载网盘

1. 新建Linux下的文件夹

   ```shell
   rm -rf /root/music  #删除已有的目录
   mkdir /root/music  #新建目录
   ```
   
2. 挂载磁盘

   下载脚本

   ```shell
   wget -N --no-check-certificate https://raw.githubusercontent.com/x91270/Centos/master/rcloned
   ```

   使用 `vim rcloned`修改脚本项

   ```
   NAME="myone" #创建的rclone名，本文此处填ojbk
   REMOTE="音乐" #远程挂载地址对应的文件夹，是你OneDrive对应的具体目录
   LOCAL="/root/music" #在本机上的挂载地址
   ```

   启动脚本 `rcloned start`

3. 挂载成功后，输入`df -h`命令查看

   ![image-20200815181741080](https://i.loli.net/2020/08/15/y2B5TYqenzbkDcX.png)
   
4. 设置开机启动

   ```shell
   mv rcloned /etc/init.d/rcloned    #移动rcloned到init(开机启动目录)下
   chmod +x /etc/init.d/rcloned      #给rcloned可执行权限
   chkconfig rcloned on                   #设置自启动
   bash /etc/init.d/rcloned start       #启动rclone
   ```

   









