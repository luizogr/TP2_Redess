# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import socket
import threading 
import sys

# Função para poder receber mensagens do outro cliente em paralelo, sem bloquear o envio de mensagens.
def receber_mensagens(socket_cliente):
    # Loop para receber mensagens
    while True:
        try:
            # Tenta receber uma mensagem do servidor
            dados = socket_cliente.recv(1024)
            if not dados:
                print("\nO servidor encerrou o chat.")
                break
            # Exibe a mensagem recebida do outro cliente
            print(f"\n[Amigo]: {dados.decode()}")
        except socket.error:
            break
    print("Finalizando recepção. Pressione Enter para fechar.")
    sys.exit()

# Criação do socket do cliente TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:    
    # Conecta ao servidor de chat
    client_socket.connect(('192.168.1.14', 7000))
    print("Conectado ao servidor de chat! Aguardando o outro participante...")

    # Cria e inicializa a thread de recepção
    thread_rec = threading.Thread(target=receber_mensagens, args=(client_socket,))
    thread_rec.daemon = True  
    thread_rec.start()

    # Loop envio de mensagens
    print("Digite suas mensagens abaixo. Para sair, digite 'sair'.")
    while True:
        mensagem = input()

        if mensagem.strip() == "":
            print("Não é permitido enviar mensagens vazias")
            continue 
        if mensagem.strip().lower() == "sair":
            break
        # Envia a mensagem para o servidor, que irá encaminhar para o outro cliente    
        client_socket.send(mensagem.encode())


except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    client_socket.close()