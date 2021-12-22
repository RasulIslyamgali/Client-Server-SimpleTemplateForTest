import datetime
import json
import socket



def start_my_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 2000))

    server.listen(4)
    print("working...")
    while True:
        try:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode("utf-8")
            print("data: ", data)
            HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")
            employee_id = data.split("id=")[-1]
            content = HDRS + f"Employee with id: {employee_id} was successful add to COLVIR\r\n\r\n".encode()


            if "POST" in data:
                client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            print(f"[INFO] Server closed with KeyboardInterrupt")
            server.close()


if __name__ == "__main__":
    start_my_server()