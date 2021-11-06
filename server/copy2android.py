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
    first = False
    second = False


def new_client(client, server):
    print("new client joined:" + client)
    clients.append(client)


def received(client, server, message):
    print(message)


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


data = Data()
clients = []
server = WebsocketServer(host=get_host_ip(), port=random.randrange(1025, 65535), loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(received)


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def on_press(key):
    pass


def on_release(key):
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
    while True:
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()


def web():
    printServerAddress()
    server.run_forever()


if __name__ == '__main__':
    t1 = threading.Thread(target=copy, name='copy')
    # https://github.com/Pithikos/python-websocket-server
    t2 = threading.Thread(target=web, name='web')
    t2.start()
    t1.start()
