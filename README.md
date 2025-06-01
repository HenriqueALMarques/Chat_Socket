**💬 Chat Socket em Python
Este é um projeto de um chat simples utilizando Sockets em Python, desenvolvido como atividade prática de redes de computadores. O projeto permite que múltiplos clientes se conectem a um servidor e conversem entre si em tempo real via terminal.

🛠️ Tecnologias Utilizadas
Python (Sockets e Threading)

Terminal / Prompt de Comando / PowerShell

Git e GitHub para versionamento

🚀 Funcionalidades
Conexão de múltiplos clientes ao servidor.

Envio de mensagens de texto entre os clientes.

Transmissão em tempo real via terminal.

Cliente pode sair a qualquer momento digitando sair.

O servidor aceita conexões simultâneas e faz o repasse das mensagens.

🗂️ Estrutura do Projeto
Pasta: Socket

servidor.py

cliente_junior.py

cliente_silva.py

cliente_antonio.py

README.md

⚙️ Como Executar
Pré-requisitos
Ter o Python instalado no computador (versão 3.x).

Ter o Git instalado (para subir no GitHub).

VS Code ou qualquer editor de sua preferência.

Passo a passo
Clone o repositório (ou baixe em ZIP).
git clone https://github.com/seu-usuario/chat-socket-python.git

Acesse a pasta do projeto.
cd chat-socket-python

Inicie o servidor.
python servidor.py

Em terminais separados, execute os clientes.
python cliente_junior.py
python cliente_silva.py
python cliente_antonio.py

Pronto! Basta digitar as mensagens no terminal de qualquer cliente e elas aparecerão nos outros.

Para sair do chat, digite sair e pressione Enter no terminal do cliente.

🔗 Funcionamento
O servidor atua como intermediário, recebendo e repassando as mensagens dos clientes. Todos os clientes conectados recebem as mensagens uns dos outros em tempo real. O servidor e os clientes utilizam o endereço 127.0.0.1 (localhost), funcionando na mesma máquina.

📜 Observações
Este é um projeto simples, sem interface gráfica, funcionando via terminal. Funciona apenas em rede local (localhost). Pode ser expandido para rodar via internet com ajustes de IP público e portas.**
