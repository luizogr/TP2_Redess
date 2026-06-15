# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import socket
import threading  

# Função para envio da mensagem de um cliente para o outro.
def encaminhar_mensagens(origem, destino, nome_origem):
    while True:
        try:
            dados = origem.recv(1024)
            if not dados:
                break
           
            destino.send(dados)
        except socket.error:
            break
    try:
        destino.close()
    except socket.error:
        pass

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(('127.0.0.1', 7000))
    server_socket.listen(2)
    print("Servidor de Chat iniciado na porta 7000. Aguardando participantes...")

    client_socket1, addr1 = server_socket.accept()
    print(f"Conexão estabelecida com: {addr1}, aguardando outro cliente")

    client_socket2, addr2 = server_socket.accept()
    print(f"Conexão estabelecida com: {addr2}, o chat começou!")

    client_socket1.send(b"Sistema: O outro usuario entrou. Podem conversar!")
    client_socket2.send(b"Sistema: Conectado ao chat. Podem conversar!")

    # t1: Tudo o que o cliente 1 falar, vai para o cliente 2
    t1 = threading.Thread(target=encaminhar_mensagens, args=(client_socket1, client_socket2, "Cliente 1"))
    # t2: Tudo o que o cliente 2 falar, vai para o cliente 1
    t2 = threading.Thread(target=encaminhar_mensagens, args=(client_socket2, client_socket1, "Cliente 2"))

    # Ativa as duas transmissões em paralelo
    t1.start()
    t2.start()

    # Faz o servidor principal esperar o chat acabar antes de fechar tudo
    t1.join()
    t2.join()

except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    server_socket.close()