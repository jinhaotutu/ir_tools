'''
@File: 
@Author: 
@version: 
@Date: 2019-12-09 12:51:24
@brief: 
@LastEditors: 
@LastEditTime: 2019-12-09 12:56:51
@attention: 
'''
import sys
import ir_tools_ui
from PyQt5.QtWidgets import QApplication, QMainWindow
from socket import *
import time
import threading
import crcmod.predefined
import json
import base64
import binascii

ui = ir_tools_ui.Ui_mainWindow()

global tools_addr
global tools_port

global find_sock
find_sock = socket(AF_INET, SOCK_DGRAM)
global data_socket
data_socket = socket(AF_INET, SOCK_STREAM)


tools_addr = '127.0.0.1'
tools_port = 8888

class ir_tools_handle(QMainWindow):

    def __init__(self):
        print("init")
        super(ir_tools_handle, self).__init__()
        self.__initUI()

    def __initUI(self):
        print("show ui")
        ui.setupUi(self)

    def closeEvent(self, QCloseEvent):
        print("exit ui")
        find_sock.close()
        data_socket.close()

def set_dis_status(sta):
    ui.listWidget_5.clear()
    ui.listWidget_5.setWordWrap(True)
    if sta == 0:
        ui.listWidget_5.addItem("搜索工具中")
    elif sta == 1:
        ui.listWidget_5.addItem("发现工具")
    elif sta == 2:
        ui.listWidget_5.addItem("连接工具中")
    elif sta == 3:
        ui.listWidget_5.addItem("已连接")
    elif sta == 4:
        ui.listWidget_5.addItem("已断开")
    ui.listWidget_5.backgroundRole()
    time.sleep(0.5)

def dis_params(num, display):
    if num == 1:
        ui.listWidget.clear()
        ui.listWidget.setWordWrap(True)
        ui.listWidget.addItem(display)
        ui.listWidget.backgroundRole()
    elif num == 2:
        ui.listWidget_2.clear()
        ui.listWidget_2.setWordWrap(True)
        ui.listWidget_2.addItem(display)
        ui.listWidget_2.backgroundRole()
    elif num == 3:
        ui.listWidget_3.clear()
        ui.listWidget_3.setWordWrap(True)
        ui.listWidget_3.addItem(display)
        ui.listWidget_3.backgroundRole()
    elif num == 4:
        ui.listWidget_4.clear()
        ui.listWidget_4.setWordWrap(True)
        ui.listWidget_4.addItem(display)
        ui.listWidget_4.backgroundRole()

def my_crc8(buf, len):
    crc_all = 0
    for i in range(len):
        crc_all += buf[i]

    return crc_all%256


# 发现设备
def tools_find(num):
    print("ir tools find")

    set_dis_status(0)

    find_addr = ('', 6407)
    find_sock.bind(find_addr)

    while True:
        print("wait find ir tools")
        data, addr = find_sock.recvfrom(1024)
        if (len(data) <= 0) | (data == 0):
            print("recvfrom fail")
            return

        print(data)
        print(addr)

        if (data[0] == 0x55) | (data[1] == 0xaa):
            print("find head")

            data_len = data[2]
            print("data_len:" + str(data_len))

            # crc = crcmod.predefined.Crc('crc-8-maxim')
            # crc.update(data[0:(data_len+3)])
            if my_crc8(data, data_len+3) == data[data_len+3]:
                find_data = data[3:3+data_len].decode('utf-8')
                print(find_data)

                find_json = json.loads(find_data)
                global tools_addr
                tools_addr= find_json["ip"]
                print(tools_addr)
                global tools_port
                tools_port= find_json["port"]
                print(tools_port)

                break


    find_sock.close()

    set_dis_status(1)

    data_thread.start()
    print(data_thread.getName())
    print("find thread exit")

# 发现设备
def tools_data(num):
    print("ir data recv")

    while True:
        set_dis_status(2)

        # data_socket = socket(AF_INET, SOCK_STREAM)

        data_addr = (tools_addr, tools_port)
        print(data_addr)
        ret = data_socket.connect(data_addr)
        if ret == 0:
            print("connect fail")
            data_socket.close()
            time.sleep(5)
            continue

        set_dis_status(3)

        while True:
            recv_data = data_socket.recv(1024*3)
            if (len(recv_data) <= 0) | (recv_data == 0):
                print("recv fail")
                break

            print(recv_data.decode('utf-8'))

            data_json = json.loads(recv_data)

            key_data = base64.b64decode(data_json["data"])

            key_hex = key_data.hex()
            print(key_hex)

            key_base64_16 = [key_data[i] | (key_data[i + 1] << 8) for i in range(0, len(key_data), 2)]
            print(key_base64_16)

            key_time = " ".join(str(i) for i in key_base64_16)

            dis_params(1, key_time)
            dis_params(2, key_hex)
            dis_params(3, str(data_json["freq"]))
            dis_params(4, str(data_json["key_cnt"]))

    data_socket.close()
    set_dis_status(4)
    time.sleep(5)
    print("data thread exit")


find_thread = threading.Thread(target=tools_find,args=(33,))
data_thread = threading.Thread(target=tools_data,args=(22,))

# 数据传输主函数
def ir_tools_main():
    print("ir tools main")

    find_thread.start()
    print(find_thread.getName())


if __name__ == '__main__':
    print(sys.platform)
    app = QApplication(sys.argv)
    MainWindow = ir_tools_handle()
    MainWindow.show()
    print("ui show")
    ir_tools_main()
    sys.exit(app.exec_())
    print("app exit")