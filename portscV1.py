
# para passar comandos para o so
import socket

portas = [80, 21, 23, 443, 8080]

#vai rodar todos os numeros
for porta in portas:
    
    #atribuindo a um objeto, o ip(AF_INET) e o tcp (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #coloca tempo em ver se a porta vai estar aberta
    client.settimeout(0.10)
    #retorna um cod
    codigo = client.connect_ex(('site', porta))
    if codigo == 0:
        print (porta, "-porta aberta")
