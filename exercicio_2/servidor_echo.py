import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 6000)
server_socket.bind(server_address)

print("Servidor UDP aguardando mensagem...")

while True:
    data, client_address = server_socket.recvfrom(65535)
    print(f"Mensagem recebida de {client_address}: {data.decode()}")

    server_socket.sendto(data, client_address)