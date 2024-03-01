import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9000))

data = cli.recv(1024)  # 最大收1024字节
print(data)
print(data.decode("utf-8"))
cli.send("收到".encode("utf-8"))

cli.close()
