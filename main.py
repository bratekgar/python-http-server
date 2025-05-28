from socket import socket, AF_INET, SOCK_STREAM

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 5604))
serverSocket.listen(1)

try:
    while True:
        print("New request!")
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            endpoint = message.split()[1].decode('utf-8').strip("/")
            connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
            print("endpoint:" + endpoint)
            if endpoint == 'home':
                connectionSocket.send('<h1>KURWAAAAAAAAAA</h1>'.encode())

            if endpoint == '':
                connectionSocket.send('<h1>JA PIDIDI ZABIJE SIE</h1>'.encode())

        except IOError:
            connectionSocket.send('404 Not Found'.encode())

        finally:
            connectionSocket.close()

except KeyboardInterrupt:
    print("debilu dałeś ctr-c aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    serverSocket.close()
