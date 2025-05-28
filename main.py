import socket


def make_get_request(host):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)

    # Connect to the host
    client_socket.connect((host, 2137))

    # Create the GET request
    request = b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n"

    # Send the GET request
    client_socket.sendall(request)

    response = b""
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
        except socket.timeout:
            break

    client_socket.close()

    return response.decode('utf-8')


if __name__ == "__main__":
    host = "www.google.com"
    response = make_get_request(host)
    print(response)
