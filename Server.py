import socket
import time

is_server_running = False

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server created on " + host + ":" + str(port))
    is_server_running = True

except:
    print("Server could not be created")

if is_server_running == True:
    while True:
        print("Listening for clients...")
        client_socket, addr = server_socket.accept()
        print("Got a connection from " + str(addr))
        current_time = time.ctime(time.time()) + "\r\n"
        client_socket.send(current_time.encode('ascii'))
        client_socket.close()