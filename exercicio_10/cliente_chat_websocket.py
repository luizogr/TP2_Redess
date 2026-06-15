# Hudson Junior Xavier da Silva, Janaina Alves Cordeiro, Luiz Otávio Gonçalves Ribeiro, Tiago Secundo Santos
import asyncio
import websockets

# Função para receber mensagens do servidor
async def receber_mensagens(websocket):
    # Loop para receber mensagens do servidor e exibi-las
    try:
        # Recebe mensagens do servidor e as exibe no console
        async for message in websocket:
            print(f"\n{message}")
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo servidor")

# Função para enviar mensagens ao servidor
async def enviar_mensagens(websocket, nome):
    loop = asyncio.get_event_loop() # Permite usar input sem bloquear a execução do loop de eventos, evitando travar a recepção de mensagens enquanto o usuário digita.
    # Loop para ler mensagens do usuário e enviá-las ao servidor
    while True:
        # Solicita ao usuário que digite uma mensagem e a envia para o servidor, permitindo que o usuário digite "sair" para encerrar a conexão
        mensagem = await loop.run_in_executor(None, input, f"[{nome}]: ") # Permite entrada de mensagens sem bloquear a recepção(usando input trava a execução)
        # Verifica se o usuário deseja sair do chat, caso contrário, envia a mensagem para o servidor
        if mensagem.lower().strip() == "sair":
            await websocket.close()
            break
        else:
            await websocket.send(mensagem)

# Função principal para conectar ao servidor e iniciar as tarefas de envio e recepção de mensagens
async def main():
    # URI do servidor WebSocket para conectar-se
    uri = "ws://192.168.1.14:9000" # Endereço para conectar ao servidor WebSocket
    # Tenta conectar ao servidor WebSocket e iniciar as tarefas de envio e recepção de mensagens
    try:
        # Conecta ao servidor WebSocket e inicia as tarefas de envio e recepção de mensagens em paralelo usando asyncio.gather
        async with websockets.connect(uri) as websocket:
            print("Conectado ao servidor de chat WebSocket!")
            nome = input("Digite seu nome: ")
            await asyncio.gather(receber_mensagens(websocket), enviar_mensagens(websocket, nome))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo servidor.")
    
asyncio.run(main())