import socket
import threading

clientes = []

def broadcast(mensagem, cliente_origem):
    for cliente in clientes:
        if cliente != cliente_origem:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def handle_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            if mensagem:
                print(f"Mensagem recebida: {mensagem.decode()}")
                broadcast(mensagem, cliente)
            else:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)
                break
        except:
            cliente.close()
            if cliente in clientes:
                clientes.remove(cliente)
            break

host = '127.0.0.1'
port = 5555

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, port))
servidor.listen()

print(f"Servidor iniciado em {host}:{port}")

while True:
    cliente, endereco = servidor.accept()
    print(f"Conectado a {endereco}")
    clientes.append(cliente)

    thread = threading.Thread(target=handle_cliente, args=(cliente,))
    thread.start()
