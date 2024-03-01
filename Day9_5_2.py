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
    server_response = cli.recv(1024).decode()  # 4-8KB之间
    while True:
        try:
            cmd_res_tuple = json.loads(server_response)
            break

        except json.decoder.JSONDecodeError:
            server_response += cli.recv(1024).decode()

    print(f"命令执行状态{cmd_res_tuple[0]}")
    print(cmd_res_tuple[1])

cli.close()