---
title: CefSharp的使用 
urlname: cefsharp_use
date: 2020-07-30 15:30:48
tags: [WPF,C#]
categories: 编程
cover: https://i.loli.net/2020/07/30/mTltYK4pQ39xqPj.png
---



之前一直使用WPF自带的`WebBrowser`控件，但由于它使用的是IE内核，巨无敌难用，还各种报错。于是换了一个开源的浏览器包CefSharp，它支持Winform和WPF，内嵌了Chrome浏览器组件并且有比较详细的说明文档。

- [开源项目地址](https://github.com/cefsharp/CefSharp)

- [官方中文帮助文档](https://github.com/cefsharp/CefSharp/wiki/CefSharp中文帮助文档)

## 安装

1. 通过Nuget安装，右击项目 -> 管理Nuget程序包 -> 在打开的界面中搜索CefSharp，依次安装 `CefSharp.Common`和 `CefSharp.Wpf` ，至于 `cef.redist.x64`和 `cef.redist.x86`会自动安装。

   ![image-20200730153609000](https://i.loli.net/2020/07/30/7NdrJnzxabOZfPh.png)

2. 配置解决方案平台

   因为CefSharp不支持ANYCPU所以要配置x86、x64，点击菜单生成 -> 配置管理器。选择解决方案平台，点击编辑，先将x64和x86删掉，再重新新建，重新配置比较容易些。

   ![image-20200730154155013](https://i.loli.net/2020/07/30/Unib4OjqVvwKB7P.png)

## 使用

使用时可以直接在xaml文件中直接添加`ChromiumWebBrowser`控件，不过一个`ChromiumWebBrowser`控件就要占几M的内存，所以代码动态添加也是一种选择。

### 在xaml中添加浏览器

1. xmal文件头部插入引用`xmlns:wpf="clr-namespace:CefSharp.Wpf;assembly=CefSharp.Wpf"`，添加控件如下：

   ```xaml
   <Grid x:Name="ctrlBrowerGrid">
       <wpf:ChromiumWebBrowser x:Name="Browser"/>
   </Grid>
   ```

2. cs文件中操作控件访问网址：

   ```c#
   Browser.Load(“www.baidu.com”);
   ```

### 动态添加浏览器

1. 添加浏览器类：

   ```c#
   internal sealed class CollapsableChromiumWebBrowser : ChromiumWebBrowser
   {
       public CollapsableChromiumWebBrowser()
       {
           this.Loaded += this.BrowserLoaded;
       }
   
       private void BrowserLoaded(object sender, System.Windows.RoutedEventArgs e)
       {
           // Avoid loading CEF in designer
           if (DesignerProperties.GetIsInDesignMode(this))
               return;
           // Avoid NRE in AbstractRenderHandler.OnPaint
           ApplyTemplate();
           CreateOffscreenBrowser(new Size(400, 400));
       }
   }
   ```

2. 动态添加和操作控件：

   ```c#
   CollapsableChromiumWebBrowser Browser = new CollapsableChromiumWebBrowser();
   //页面插入控件
   ctrlBrowerGrid.Children.Add(Browser);
   //这里不能用Load()的方法，会报错。
   Browser.Address = “www.baidu.com”; 
   ```

### 获取Cookie和Html

1. 添加Cookie访问类

   ```c#
   public class CookieVisitor : ICookieVisitor
   {
       public static string Cookies = null;
       public static string Html = null;
       public event Action<object> Action;
       public bool Visit(CefSharp.Cookie cookie, int count, int total, ref bool deleteCookie)
       {
           if(count == 0)
               Cookies = null;
           
           Cookies += cookie.Name + "=" + cookie.Value + ";";
           deleteCookie = false;
           return true;
       }
   
       public void Dispose() 
       {
           if (Action != null)
               Action((Html, Cookies));
           return;
       }
   }
   ```

2. 添加Cookie和Html获取回调函数

   ```c#
   public async void RecieveCookie(object data)
   {
       (string html,string cookies) = ((string,string))data;
       return;
   }
   ```

3. 浏览器控件访问网址，并设置回调

   ```c#
   async void LoadWebBrowser()
   {
       Browser.FrameLoadEnd += Browser_FrameLoadEnd;
       Browser.Address = "www.baidu.com";
   }
   
   private async void Browser_FrameLoadEnd(object sender, FrameLoadEndEventArgs e)
   {
       CookieVisitor.Html = await Browser.GetSourceAsync();
       CookieVisitor visitor = new CookieVisitor();
       visitor.Action += RecieveCookie;
       Cef.GetGlobalCookieManager().VisitAllCookies(visitor);
       return;
   }
   ```

   

