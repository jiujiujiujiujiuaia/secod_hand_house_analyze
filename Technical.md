## 技术实现
首先，我还是想像之前破解”俺来也“app一样：
* 1.笔记本配置Finddler环境
* 2.手机配置抓包环境
* 3.抓包，找到对应接口
* 4.通过jadx-gui反编译apk应用，然后进行接口破解，找到客户端代码如何鉴权，如何加盐

但是我低估了上面的难度，首先我对client端的框架不理解，然后反编译的时候代码无法跳转
，对代码阅读增加了难度，最后尽管找到了鉴权的地方，但是还是没能破解。

山穷水尽疑无路，没想到在CSDN上找到一段代码，通过爬取web端接口，非常简单的使用cookie
就能拿到成交价的所有信息，令人大喜过望。

## TODO