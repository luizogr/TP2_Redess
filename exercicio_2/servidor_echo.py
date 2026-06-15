# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
# Importa o módulo socket para comunicação em rede
import socket

# === CONFIGURAÇÃO DO SERVIDOR UDP ===
# Cria um socket UDP (SOCK_DGRAM)
# Este é um servidor "Echo": repete tudo que recebe
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereço e porta onde o servidor UDP irá escutar
server_address = ('0.0.0.0', 6000)

# Vincula o socket ao endereço e porta definidos
# bind() para UDP é similar ao bind() em TCP, mas UDP é connectionless
server_socket.bind(server_address)

print("Servidor UDP aguardando mensagem...")

# === LOOP PRINCIPAL DO SERVIDOR ===
# Loop infinito aguardando mensagens de clientes
while True:
    # recvfrom() recebe um datagram UDP
    # Retorna (dados, endereço_cliente) onde endereço_cliente = (IP, porta)
    # Máximo 65535 bytes por datagram
    data, client_address = server_socket.recvfrom(65535)
    print(f"Mensagem recebida de {client_address}: {data.decode()}")

    # Echo: envia os mesmos dados de volta para o cliente
    # sendto() envia dados UDP para um endereço específico
    server_socket.sendto(data, client_address)