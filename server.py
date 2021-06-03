from os import waitpid
import queue
import socket
import threading
import time
import pdb
from queue import Queue

host = 'localhost'
port = 5052
kuyruk= Queue()

list = []
listaddr = []



try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket olusturuldu. [ + ]")

    s.bind((host,port))
    print(f"Socket {port} nolu porta baglandi.")

    s.listen(5)
    print("Socket dinleniyor")

except socket.error as msg:
    print("Hata!", msg)


def mesajreturn():
    msg = str(input("\nMesaj to client :  "))
    if msg is None:
        time.sleep(9999)
    else:
        return msg


def kontrol(c, addr):
    len=connlen()
    if (len >= 2):
        check(len)
    else:
        NewSocket(c, addr)

def NewSocket(c, addr):
    try:   
        while True:
            mesaj = str(input("\nMesaj to client : "))
            c.send(mesaj.encode("utf-8"))
            break
        kontrol(c, addr)
        
        #t.join()
            #yanit = c.recv(1024)
            #print(f"Bu mesaj soketten {addr}: ", yanit.decode("utf-8"))    
    except Exception as msg:
        print(f"Hata ! {addr} ", msg)
        exit()

def connections():
    s = 0
    for x in listaddr:
        print(f"\n[{s}] {x}\n")
        s+=1
    try:
        secim=int(input("\nSecim : "))
        if (secim == 0 ):
            return 0
        elif (secim == 1):
            return 1
        else:
            print("Yanlis deger girdiniz!")
            time.sleep(3)
            connections()
    except Exception as msg:
        print(F"Hata ! {msg}")
        connections

def connlen():
    i=0
    for x in list:
        i+=1
    return i

def list_get(len):
    if len == 0 :
        x = list[0]
        return x
    elif len == 1:
        x = list[1]
        return x

def listaddr_get(len):
    if len == 0 :
        x = listaddr[0]
        return x
    elif len == 1:
        x = listaddr[1]
        return x

def check(lenlist):
    if lenlist >= 2:
        k = connections()
        x = list_get(k)
        z = listaddr_get(k)
        NewSocket(x,z)
    else:
        pass



while True:
    try:
        c, addr = s.accept()
        list.append(c)
        listaddr.append(addr)
        
        print("\nGelen baglanti ", addr)
        t=threading.Thread(target=kontrol, args = ((c, addr)))
        t.start()
        
    except Exception as msg:
        print("Hata! ", msg)

s.close()
