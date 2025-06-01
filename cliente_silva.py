import socket
import threading

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            print(mensagem)
        except:
            print("Desconectado do servidor.")
            cliente.close()
            break

host = '127.0.0.1'
port = 5555

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

nome = "Silva"

thread_receber = threading.Thread(target=receber)
thread_receber.start()

while True:
    mensagem = input()
    if mensagem.lower() == 'sair':
        cliente.close()
        break
    mensagem_formatada = f"{nome}: {mensagem}"
    cliente.send(mensagem_formatada.encode())
