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
        cmd = conn.recv(1024)  # 阻塞的
        if not cmd:  # 代表客户端断开
            break
        # 执行指令，拿到结果，并发送给客户端
        print(f"From client {client_addr}: {cmd.decode()}")
        cmd_res = subprocess.getstatusoutput(cmd.decode())

        send_bytes = conn.send(json.dumps(cmd_res).encode())
        print("Generate:", len(json.dumps(cmd_res).encode()))
        print("Send:", send_bytes)

    if count > 2:
        break

s.close()
