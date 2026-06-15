# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import socket

# Configuração do cliente TCP para solicitar a hora ao servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenta conectar ao servidor de hora e receber a mensagem com a hora atual
try:    
    # Conecta ao servidor de hora
    client_socket.connect(('10.2.212.11', 8000))

    # Aguarda a mensagem do servidor com a hora atual 
    message_server = client_socket.recv(1024)
    # Exibe a mensagem recebida do servidor, que contém a hora atual
    print(message_server.decode())

except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    client_socket.close()