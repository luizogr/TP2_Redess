# Importa o módulo socket para comunicação em rede
import socket

# === CONFIGURAÇÃO DO SERVIDOR ===
# Cria um socket TCP (SOCK_STREAM) para comunicação IPv4 (AF_INET)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Vincula o servidor ao IP local (127.0.0.1) e porta 5000
    # O servidor agora "escuta" nesse endereço e porta
    # Qualquer cliente que tentar conectar nessa porta será aceito
    server_socket.bind(('127.0.0.1', 5000))

    # Coloca o servidor em modo de escuta
    # O argumento 5 é o número máximo de conexões pendentes na fila
    # Se 5 clientes tentarem conectar simultaneamente, apenas 5 ficarão na fila
    server_socket.listen(5)
    print("Servidor esperando conexões...")

    # Loop infinito - o servidor funciona continuamente
    while True:
        # accept() bloqueia a execução até que um cliente se conecte
        # Retorna dois valores:
        # - client_socket: novo socket para comunicação com esse cliente
        # - addr: tupla com (IP, porta) do cliente
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com: {addr}")

        try:
            # Recebe a mensagem do cliente (máximo 1024 bytes)
            # recv() bloqueia até receber dados ou conexão fechar
            message = client_socket.recv(1024)
            
            # Verifica se recebeu alguma mensagem
            if not message:
                print(f"Sem mensagem do cliente: {addr}")
            else:
                # Decodifica os bytes para string
                mensagem_cliente = message.decode()
                print(f"Mensagem do cliente: {mensagem_cliente}")
                
                # Envia resposta para o cliente
                # b"..." cria bytes literalmente (string com prefixo 'b')
                client_socket.send(b"Bem-vindo ao servidor! Mensagem recebida")
        
        # Captura erros que possam ocorrer durante a comunicação com o cliente
        except socket.error as e:
            print(f"Erro na mensagem do cliente")

        # Fecha a conexão com esse cliente após terminar a comunicação
        # Importante: apenas fecha a conexão com o cliente, não o servidor
        # O servidor continua rodando no loop while True
        finally:
            client_socket.close()

# Captura erros ao vincular o servidor (ex: porta já em uso)
except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

# Garante que o socket servidor seja fechado ao fim do programa
# Libera a porta 5000 para que possa ser reutilizada
finally:
    server_socket.close()