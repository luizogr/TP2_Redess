# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
# Importa o módulo socket para comunicação em rede
import socket

# === CONFIGURAÇÃO DO CLIENTE ===
# Cria um socket TCP (SOCK_STREAM) para comunicação IPv4 (AF_INET)
# AF_INET = Protocolo IPv4
# SOCK_STREAM = Conexão TCP confiável (em contraste com UDP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:    
    # Tenta conectar ao servidor na máquina local (127.0.0.1) porta 5000
    # 127.0.0.1 = localhost (própria máquina)
    # 5000 = porta onde o servidor está escutando
    client_socket.connect(('127.0.0.1', 5000))

    # Solicita ao usuário que digite uma mensagem
    mensagem = input("Digite a mensagem ao servidor: ")

    # Valida se a mensagem não está vazia
    # strip() remove espaços em branco da mensagem
    if mensagem.strip() == "":
        print("Não é permitido enviar mensagens vazias")
    else:
        # Converte a string para bytes usando encode() e envia ao servidor
        # Necessário converter porque sockets trabalham com bytes, não strings
        client_socket.send(mensagem.encode())
        
        # Recebe a resposta do servidor (máximo 1024 bytes)
        # recv(1024) fica aguardando até receber dados do servidor
        message_server = client_socket.recv(1024)
        
        # Decodifica os bytes recebidos de volta para string e exibe na tela
        # decode() converte bytes para string usando codificação padrão (UTF-8)
        print(f"Mensagem do servidor: {message_server.decode()}")

# Captura erros de socket (conexão recusada, timeout, etc.)
except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

# Garante que o socket seja fechado mesmo se ocorrer um erro
# Importante para liberar recursos da conexão
finally:
    client_socket.close()