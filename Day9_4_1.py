import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9000))
s.listen(2)

count = 0
while True:  # 为了不断接收新连接
    conn, client_addr = s.accept()
    count += 1
    print(f"[{count}]Got a new connection: {client_addr}")

    while True:
        data = conn.recv(1024)  # 阻塞的
        if not data:  # 代表客户端断开
            break
        print(f"From client {client_addr}: {data.decode()}")
        conn.send(data.decode().upper().encode())

    if count > 2:
        break

s.close()
