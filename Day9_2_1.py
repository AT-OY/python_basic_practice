import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 9000))
s.listen()  # 允许挂起多少个连接
client_conn, client_addr = s.accept()  # 等待客户端连接，当一个连接进来，就会为这个连接生成一个专门的实例
print(client_conn, client_addr)

client_conn.send("Hello,你来了？".encode("utf-8"))  # 只能接受字节类型，发数据给客户端
data = client_conn.recv(1024)  # 从客户端收数据，收1024字节
print(data)
print(data.decode("utf-8"))

client_conn.close()  # 关掉跟客户端的连接

s.close()  # 关掉服务器
