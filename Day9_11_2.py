import socket
import json

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9000))


def progress_bar(totl_size):
    received_percent = 0
    while received_percent <= 100:
        recv_size = yield  # 在这里中断，返回到主流程上，send会重新唤醒生成器，并传值给yield
        new_percent = round((recv_size / totl_size) * 100)
        if new_percent > received_percent:
            print(f"\r[{new_percent}% {new_percent * '>'}]", end="", flush=True)
            received_percent = new_percent


while True:
    cmd = input("Input cmd >> ").strip()
    if not cmd:
        continue
    if cmd == "q":
        break
    cli.send(cmd.encode())

    # 1. 接收固定消息头
    raw_msg_head = cli.recv(32).decode()
    # 2. 拿到文件大小和文件名
    file_size = int(raw_msg_head.split("|")[1])
    file_name = cmd.split()[1]
    p = progress_bar(file_size)  # 生成一个进度条对象
    p.__next__()  # 启动
    # 3. 在本地创建一个文件，文件名.download
    f = open(f"{file_name}.download", mode="wb")
    # 4. 循环接收数据
    received_size = 0
    while received_size < file_size:
        raw_data = cli.recv(1024)  # 有可能收不满
        received_size += len(raw_data)
        f.write(raw_data)
        p.send(received_size)
    f.close()
    print("\nTransmission Finish")
cli.close()
