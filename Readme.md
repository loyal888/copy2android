# Introduce

**This project,support you copy from Mac,and paste it on Android.**  The data only support LAN,not
over cross Internet.

Not support for iphone,because this feature implemented by Apple,Inc.

# How to use?

//TODO

# How it works?

- Firstly,we need monitor the `command + c`,and get the content.

  - how to monitor?
    - using python script and get the clipboard content.
- And when we get the clipboard content,we send the content to your android devices.

  - how to send?
    - By using **WebSocket**.To achieve communicating between Mac and Android devices, we need a
      web-socket server,when we get the clipboard content,we sent it to android device.
- When we got the content from server, we write it to android clipboard
- Now,we can paste on Android devices!

# Future Plan?

- copy from android,paste on Mac.

# 介绍

**支持你从Mac复制，粘贴到Android** 

> *数据只支持局域网传输，不通过互联网传输。 不支持iphone，因为此功能已经由Apple，Inc.实现。*

# 如何使用？

//待办事项

# 它是如何工作的？

- 首先，我们需要监视`command+c`，并获取内容。
  - 如何监控？
    - 使用python脚本并获取剪贴板内容。
    - 当我们获得剪贴板内容时，我们会将内容发送到您的android设备。
  - 如何发送？
    - 通过使用**WebSocket**。实现Mac和Android设备之间的通信， 我们需要一个web套接字服务器，当我们获得剪贴板内容时，我们将其发送到android设备。
    - 当我们从服务器获取内容时，我们将其写入android剪贴板
- 现在，我们可以在Android设备上粘贴了！

# 未来计划？

- 从android复制，粘贴到Mac上。
