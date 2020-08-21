---
title: VS调试Linux程序环境配置
urlname: vs_linux_debug
date: 2020-06-21 19:01:17
tags: 
  - vs
  - linux
categories: 
  - 软件
cover: https://i.loli.net/2020/06/22/72xVdFeCENnyG4O.jpg
top: False
---

## 基础配置

1. Linux安装调试器

   ```shell
   sudo apt-get install openssh-server g++ gdb gdbserver
   ```

2. Windows环境配置

   - Linux C++调试组件安装
     
     ![vstool](https://i.loli.net/2020/06/22/1dVF5TKPo3W8tsp.png)

   - Linux头文件拷贝到Windows

     Linux的头文件目录为：/usr/include   

     Windows的目录为：安装目录\Common7\IDE\VC\Linux\include\usr\include

     注：拷贝之前最好先备份一下windows的头文件目录

   - VS配置

     增加Linux程序编译时的信息输出，以便更容易查看错误信息，打开路径"菜单-工具-选项-项目和解决方案-生成并运行"，更改MSBuild的两个选项改为普通
     
     ![MSBuild](https://i.loli.net/2020/06/22/3HrUAYFdV6GE4lh.png)

     添加Linux的IP与端口，使用SSH连接，打开路径"菜单-工具-选项-Cross Platform"
     
     ![linuxssh](https://i.loli.net/2020/06/22/yoaX9reUzTCVWKQ.png)

## 测试工程

1. 新建Linux工程
   
   ![linuxpro](https://i.loli.net/2020/06/22/FdYG23qugl7bZEy.png)

2. 测试代码

   ```c++
   #include <cstdio>
   #include <cstdlib>
   #include <string.h>
   #include <pthread.h>
   void* func(void* arg)
   {
          printf("HELLO WORLD - VS LINUX!");
          return NULL;
   }
   int main()
   {
          pthread_t handle;
          pthread_create(&handle, NULL, func,NULL);
          pthread_join(handle, NULL);
          return 0;
   }
   ```

3. 修改项目配置

   - 路径：右键项目-属性-C/C++-所有选项 
     
      a. 检查linux是否支持C11，如果不支持的话，要改为C99之类
      
      b. 附加选项增加多线程所需要的标识‘-lphread’
      
   - 路径：右键项目-属性-链接器-所有选项 
     
      a. 附加选项增加多线程所需要的标识‘-lphread’
      
   - 路径：右键项目-属性-常规  
     
      a. 远程生成根目录（默认生成地址为~/project，这里可以修改成自己的专属目录地址）
      
   - 路径：右键项目-属性-调试  
     
      a. 调试模式（默认为gdbserver，需要看看自己的linux是否支持，如果不支持要改成gdb）
      
      ![vsset1](https://i.loli.net/2020/06/22/wQSsTkGa6IhZKyu.png)
      
      ![vsset2](https://i.loli.net/2020/06/22/h8iqXyV3cE7mBOa.png)
      
      ![vsset3](https://i.loli.net/2020/06/22/XvDc982jJdqg7C6.png)
4. 调试

   路径：菜单-调试-linux console，可以查看printf输出的信息，linux上需要安装gdbserver才能看到输出的信息

5. 链接库的配置

   比如：工程需要链接静态库  /root/projects/xxxxxxxx.a

   ![vslib](https://i.loli.net/2020/06/22/fqjKJQx7EPCIXWv.png)
