# 项目介绍
# 使用python发包实现江苏大学系统登陆（不是利用自动化，直接破破解滑块登陆、密码加密）此项目只是为了学习交流，请勿传播Thank you。

思路：江苏大学登录系统通过F12抓包可以看到账号没有加密，但是密码进行了加密，并且在这个过程当中是有滑块进行验证的一个过程。所以在这个过程当中我们只需要通过发包模拟加密和滑块验证的过程就可以实现登录的一个过程。
F12抓包如下图所示： \
<img width="835" alt="image" src="https://github.com/user-attachments/assets/7ebb4610-1814-446c-a103-e30a0ae8b0f4" />

username:学号名 \
password：加密后的密码 \
lt: 参数1 \
dllt: 参数2 \
execution: 参数3 \
_eventId: 参数4 \
rmShown: 参数5 \
sign: 滑块验证后生成的值 \

## demo.py进行密码解密和加密的过程
当中会进行cookie的保存，以及上述参数的获取、调用open_cv当中的函数进行滑块验证后返回验证后的sign值。
## open_cv.py 进行滑块验证的一个过程
进行滑块验证后得到sign值返回给demo.py最后实现请求头的携带。
## node1.js和node.js是为了完成密码的一个逆向解密

## 上述两个过程都已经执行成功后会输出一个“找到的文本: 在校学生”表示已经登陆成功了，并将登陆成功的cookie保存在了cookie.txt文件当中，后续还想对登陆后的其他页面进行数据获取时只需要携带这个cookie在请求头当中即可。

将文件下载下来后拷贝到一个目录下，然后安装好对应requirements.txt当中的库后,手动执行demo.py查看打印结果即可

