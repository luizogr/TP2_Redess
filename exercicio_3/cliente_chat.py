# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import socket
import threading 
import sys

# Função para poder receber mensagens do outro cliente em paralelo, sem bloquear o envio de mensagens.
def receber_mensagens(socket_cliente):
    while True:
        try:
            dados = socket_cliente.recv(1024)
            if not dados:
                print("\nO servidor encerrou o chat.")
                break
            print(f"\n[Amigo]: {dados.decode()}")
        except socket.error:
            break
    print("Finalizando recepção. Pressione Enter para fechar.")
    sys.exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:    
    client_socket.connect(('127.0.0.1', 7000))
    print("Conectado ao servidor de chat! Aguardando o outro participante...")

    # Cria e inicializa a thread de recepção
    thread_rec = threading.Thread(target=receber_mensagens, args=(client_socket,))
    thread_rec.daemon = True  
    thread_rec.start()

    # Loop envio de mensagens
    while True:
        mensagem = input("Digite sua mensagem (ou 'sair' para encerrar): ")

        if mensagem.strip() == "":
            print("Não é permitido enviar mensagens vazias")
            continue 
        if mensagem.strip().lower() == "sair":
            break
            
        client_socket.send(mensagem.encode())


except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    client_socket.close()