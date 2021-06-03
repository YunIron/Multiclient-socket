import socket

s = socket.socket()

host = 'localhost'
port = 5052

try:
    s.connect((host, port))
    
    while True:
        print("Mesaj bekleniyor...\n")
        yanit = s.recv(1024)
        print(yanit.decode("utf-8"))
        
        # msg = str(input("Mesaj to server :  "))
        # s.send(msg.encode("utf-8"))

except socket.error as msg:
    print("Hata !", msg)
    s.close()