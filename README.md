> ================================================================
>    Copyright (C) 2015 All rights reserved.
>
>    filename:README.md
>
>    author:sulit sulitsrc@163.com
>
>    modify date,time:2015-05-27 09:16
>
>    discription:
>
> ================================================================

fdfspyclient
======

fdfspyclient.c 是为fastdfs分布式文件系统写的部分python接口

1. 首先获得fastdfs源代码，获取地址https://github.com/happyfish100/fastdfs/archive/V5.05.tar.gz

2. 解压下载的压缩包
	```
	tar zxvf V5.05.tar.gz
	```
3. 进入源码目录，查看INSTALL文件，并安装好一切环境

4. 进入client目录，拷贝这个fastdfspyclient到client目录下，然后进入myfdfspyclient目录执行make，最后会得到一个fdfspyclient.so文件

5. 在myfdfspyclient目录下有fdfstest.py测试文件

fdfspyclient interfaces
======

[接口](interfaces.md)
