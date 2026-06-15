# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import socket
import threading
from datetime import datetime

# Função para enviar a hora atual para o cliente e registrar no log.
def enviar_hora(cliente_socket):
    # Obtém a hora atual e formata a mensagem para enviar ao cliente
    hora_atual = datetime.now().strftime("%H:%M:%S")
    mensagem = f"Sistema: A hora atual é {hora_atual}"
    # Tenta enviar a mensagem para o cliente e registra no log
    try:
        # Envia a mensagem com a hora atual para o cliente
        cliente_socket.send(mensagem.encode())
        # Registrar no log a hora enviada e o cliente que recebeu
        with open("log_hora.log", "a") as log_file:
            log_file.write(f"{datetime.now()}: Enviada hora para cliente {cliente_socket.getpeername()}\n")
    except socket.error as e:
        print(f"Erro ao enviar a hora para o cliente: {e}")
    finally:        
        cliente_socket.close()

# Configuração do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inicia o servidor e aguarda conexões
try:
    # Vincula o servidor à porta 8000 e começa a escutar por conexões
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(5)
    print("Servidor de Hora iniciado na porta 8000.")

    # Loop para aceitar conexões e criar threads para cada cliente
    while True:
        # Aceita uma conexão de cliente
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com: {addr}")
        # Criar e iniciar uma thread para enviar a hora ao cliente
        t1= threading.Thread(target=enviar_hora, args=(client_socket,))
        t1.start()

except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    server_socket.close()