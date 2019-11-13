import socket
import time
import Distance as lp
#creat a tcp/ip socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#t=lp.getCharacteristic()
#print(t)
#connect the socket to the port where the server is listening
server_address=('localhost',8080)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)


try:
    message=lp.getCharacteristic()
    print("sending %s" % message)
    sock.sendall(message.encode())

    #look for the response
    amount_received=0
    amount_expected=len(message)

    while amount_received<amount_expected:
        data=sock.recv(1024)
        amount_received+=len(data)
        print("received %s" % data.decode())
        
    while True:
        time.sleep(1)
        sock.sendall(lp.getCharacteristic().encode())
        
        
finally:
    print("closing socket")
    sock.close()

