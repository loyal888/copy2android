import random
import socket
import threading

from pynput import keyboard
import io
import qrcode
import subprocess

import logging
from websocket_server import WebsocketServer


class Data:
    """
    用来记录按键按下的是Command + C
    """
    first = False
    second = False


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def getClipboardData():
    """
    获取剪切板数据
    """
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def on_press(key):
    pass


def on_release(key):
    """
    按键释放回调
    """
    if '{0}'.format(key).lower() == '\'c\'':
        data.first = True
    if '{0}'.format(key) == 'Key.cmd':
        data.second = True
    if data.first and data.second:
        server.send_message_to_all(str(getClipboardData().decode('UTF-8')))
        data.first = False
        data.second = False
    if key == keyboard.Key.esc:
        return False


def printServerAddress():
    # print QRCode
    print(u"======================================================")
    print(u"Scan QR code to connect to server \n扫描二维码连接服务器")
    print(u"Server address: ws://" + server.host + ":" + str(server.port))
    print(u"======================================================")
    qr = qrcode.QRCode(box_size=1, border=1)
    qr.add_data("ws://" + server.host + ":" + str(server.port))
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())


def copy():
    """
    监听用户按键
    """
    while True:
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()


def new_client(client, server):
    """
    有新客户端加入回调
    :param client: 客户端
    :param server: 当前server
    :return: null
    """
    print("new client joined:" + client)


def received(client, server, message):
    """
    服务端收到客户端的消息回调
    """
    print(message)


def web():
    """
    开启WebSocket Server
    """
    printServerAddress()
    server.run_forever()


data = Data()
server = WebsocketServer(host=get_host_ip(), port=random.randrange(1025, 65535), loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(received)

if __name__ == '__main__':
    t1 = threading.Thread(target=copy, name='copy')
    # https://github.com/Pithikos/python-websocket-server
    t2 = threading.Thread(target=web, name='web')
    t2.start()
    t1.start()
