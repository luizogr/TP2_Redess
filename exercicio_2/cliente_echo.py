import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(5.0)

server_address = ('127.0.0.1', 6000)

sair = False
while sair == False:
    print("Digite 'sair' para encerrar")
    mensagem = input("Digite a mensagem ao servidor: ")

    if mensagem.strip() == "":
        print("Não é permitido enviar mensagens vazias")
    elif mensagem.strip().lower() == "sair":
        sair = True
    else:
        try:
            client_socket.sendto(mensagem.encode(), server_address)

            message_server, addr = client_socket.recvfrom(65535)
            print(f"Mensagem do servidor: {message_server.decode()}")
        except socket.timeout:
            print("Limite de tempo expirado")
            

client_socket.close()