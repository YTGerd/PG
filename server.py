import socket 

#creat a tcp/ip socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket to the port
server_address=('',8080)
print("starting up on %s poot %s" % server_address)
sock.bind(server_address)

#listen fir incomming connections
sock.listen(10)

while True:
    #wait for connection
    print("waiting for a connection.....")
    connection,client_address=sock.accept()

    try:
        print("connection from",client_address)
        while True:
            data=connection.recv(1024)
            print("received %s" % data.decode())
            if data:
                print("sending data back to the clien")
                connection.sendall(data)
            else:
                print("no more data from",client_address)
                break
    finally:
        connection.close()

    
