import os
import socket
import subprocess
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9000))
s.listen(2)

count = 0
while True:  # 为了不断接收新连接
    conn, client_addr = s.accept()
    count += 1
    print(f"[{count}]Got a new connection: {client_addr}")

    while True:
        cmd_raw = conn.recv(1024)  # 阻塞的
        if not cmd_raw:  # 代表客户端断开
            break
        # 执行指令，拿到结果，并发送给客户端
        cmd = cmd_raw.decode()
        print(f"From client {client_addr}: {cmd}")

        if cmd.startswith("get"):
            file_name = cmd.split()[1]
            if os.path.isfile(file_name):
                file_size = os.path.getsize(file_name)
                # 生成消息头
                msg_head = f"|{file_size}".zfill(32)
                head_size = conn.send(msg_head.encode())
                # print("Head:", msg_head)
                # print("Head size:", head_size)
                # 打开文件，循环发送
                f = open(file_name, "rb")
                for line in f:
                    conn.send(line)
                f.close()
                print(f"File {file_name} has been sent, size {file_size}")

            else:
                pass

    if count > 2:
        break

s.close()
