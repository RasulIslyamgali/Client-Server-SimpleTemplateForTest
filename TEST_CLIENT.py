import socket
from time import sleep

host = '127.0.0.1'
port = 2000
id_ = 12345678


def send_report_to_website(host: str, port: int, emp_id: int) -> (bool, str):
    sended_status = False
    # create socket
    print('[INFO] Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('[INFO] Failed to create socket')
        return sended_status

    print('[INFO] Getting remote IP address')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('[INFO] Hostname could not be resolved. Exiting')
        try:
            s.close()
        except:
            return sended_status
        return sended_status

    # Connect to remote server
    print(f'[INFO] Connecting to server, {host} {remote_ip}')
    s.connect((remote_ip, port))

    # Send data to remote server
    print('[INFO] Sending data to server')
    # request = "GET / HTTP/1.1\r\n\r\n"


    request = f"""POST / HTTP/1.1
    Host: foo.com
    Content-Type: application/x-www-form-urlencoded=
    Content-Length: {len(str(emp_id)) + 3}
    
    id={emp_id}""".encode()

    try:
        s.sendall(request)
    except socket.error:
        print('Send failed')
        return sended_status

    # Receive data
    print('[INFO] Receive data from server')
    reply = s.recv(1024).decode()

    print(reply)
    print(f"[INFO] Connection is closed\r\n")
    try:
        s.close()
    except:
        pass

    sended_status = True
    return sended_status, reply


if __name__ == "__main__":
    while True:
        status, response = send_report_to_website(host=host, port=port, emp_id=id_)
        if status and "successful" in response and id_ in response:
            print(f"Report about employee with id: {id_} is successful sended to {host}:{port}\r\n\r\n")
            break
        else:
            sleep(0.5)
