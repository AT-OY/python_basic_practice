import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9000))

while True:
    msg = input("Input msg >> ").strip()
    if not msg:
        continue
    if msg == "q":
        break
    cli.send(msg.encode())

    server_response = cli.recv(1024)
    print(f"From server: {server_response.decode()}")

cli.close()