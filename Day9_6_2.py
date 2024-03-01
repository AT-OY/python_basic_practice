import socket
import json

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9000))

while True:
    cmd = input("Input cmd >> ").strip()
    if not cmd:
        continue
    if cmd == "q":
        break

    cli.send(cmd.encode())

    # 1. 接收命令的长度
    res_len = int(cli.recv(1024).decode())
    print(res_len)
    # 2. 接收实际的结果
    received_size = 0
    cmd_result = ""
    # 循环接收
    while received_size < res_len:
        raw_data = cli.recv(1024)  # 有可能收不满
        cmd_result += raw_data.decode()
        received_size += len(raw_data)
        print(res_len, received_size)

    print(json.loads(cmd_result)[1])

cli.close()
