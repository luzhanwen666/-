# -
使用python发包实现江苏大学系统登陆（不是利用自动化，直接破破解滑块登陆、密码加密）核心代码不会上传，有需要联系

思路：江苏大学登录系统通过F12抓包可以看到账号没有加密，但是密码进行了加密，并且在这个过程当中是有滑块进行验证的一个过程。所以在这个过程当中我们只需要通过发包模拟加密和滑块验证的过程就可以实现登录的一个过程。
F12抓包如下图所示：
<img width="835" alt="image" src="https://github.com/user-attachments/assets/7ebb4610-1814-446c-a103-e30a0ae8b0f4" />
username:学号名
password：加密后的密码
lt: 参数1
dllt: 参数2
execution: 参数3
_eventId: 参数4
rmShown: 参数5
sign: 滑块验证后生成的值

## demo.py进行密码解密和加密的过程

## open_cv 进行滑块验证的一个过程

