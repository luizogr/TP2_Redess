# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
# Importa o módulo socket para comunicação em rede
import socket

# === CONFIGURAÇÃO DO CLIENTE UDP ===
# Cria um socket UDP (SOCK_DGRAM) em vez de TCP
# UDP = Datagram Protocol (mais rápido, mas sem garantia de entrega)
# AF_INET = Protocolo IPv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define um timeout de 5 segundos para recebimento de dados
# Se nenhuma resposta chegar em 5 segundos, lança exceção socket.timeout
client_socket.settimeout(5.0)

# Define o endereço e porta do servidor UDP
server_address = ('127.0.0.1', 6000)

# === LOOP PRINCIPAL DO CLIENTE ===
# Continua enviando mensagens até o usuário digitar 'sair'
sair = False
while sair == False:
    print("Digite 'sair' para encerrar")
    mensagem = input("Digite a mensagem ao servidor: ")

    # Valida se a mensagem está vazia
    if mensagem.strip() == "":
        print("Não é permitido enviar mensagens vazias")
    # Verifica se o usuário quer sair
    elif mensagem.strip().lower() == "sair":
        sair = True
    else:
        try:
            # sendto() envia os dados UDP para o servidor
            # Diferente de TCP (connect + send), UDP é "connectionless"
            # Não precisa estabelecer conexão antes de enviar
            client_socket.sendto(mensagem.encode(), server_address)

            # recvfrom() recebe dados UDP e retorna (dados, endereço_origem)
            # Máximo 65535 bytes (tamanho máximo de um datagram UDP)
            message_server, addr = client_socket.recvfrom(65535)
            print(f"Mensagem do servidor: {message_server.decode()}")
        # Captura timeout se o servidor não responder em 5 segundos
        except socket.timeout:
            print("Limite de tempo expirado")
            
# Fecha o socket UDP
client_socket.close()