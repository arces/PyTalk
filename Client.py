import socket

is_client_connected = False

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    client_socket.connect((host, port))
    print("Connected to server")
    is_client_connected = True
except:
    print("Could not connect to server")

if is_client_connected == True:
    current_time = client_socket.recv(1024)
    client_socket.close()
    print("Curernt time is: " + current_time.decode('ascii'))
