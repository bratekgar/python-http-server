import socket

HOST = '127.0.0.1'
PORT = 2137

html_index = "<h1>Index</h1>"
html_home = "<h1>Home</h1>"


def handle_request(path):
    if path == "/":
        return html_index
    elif path == "/home":
        return html_home
    else:
        return "<h1>404 Not Found</h1>"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            if not request:
                continue

            # Parse first line for eg. "GET / HTTP/1.1"
            lines = request.splitlines()
            if len(lines) == 0:
                continue
            first_line = lines[0]
            method, path, _ = first_line.split()

            # Generating answer
            body = handle_request(path)
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )

            conn.sendall(response.encode())
