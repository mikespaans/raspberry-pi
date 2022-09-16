import paramiko
import tkinter as tk
from functools import partial
from tkinter.messagebox import showerror
from os.path import exists
import os
import time

window = tk.Tk()
window.geometry("600x400")
window.title("Tablet Connecter")
window.configure(background="lightgrey")

host = "192.168.1.100"
port = 2222
# username = "Lenovo Tab M10 FHD Plus"
# password = "password"



def DeleteFile(Path):
    # Bestand in de tablet verwijderen 
    Path = Path.get()
    # sftp.remove(Path)
    # storage/emulated/0/Download/testweg.png -- testpad
    print ("File has been removed")

def SendFile(Path):
    # bestand vanaf de pi naar de tablet toe sturen
    # sftp.put("/home/mike/test/testfile.txt", "/storage/emulated/0/Download/testfile.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
    print ("The file has been transfered to your device")

def ReceiveFile(Path):
    # bestand van de tablet naar de pi sturen
    # sftp.get("/storage/emulated/0/Download/terugsturen.txt", "/home/mike/test/terugsturen.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
    print ("the file has been downloaded")


def AskPath(ChoosenFunction):
    AskWhatToDo.destroy()
    Textbox.destroy()
    ConnectButton.destroy()

    AskWichPath = tk.Label(window,background="lightgrey", text="Vul het pad in")
    AskWichPath.place(x=200, y=30)

    Path = tk.StringVar()

    TextBoxPath = tk.Entry(window, width=30, textvariable=Path)
    TextBoxPath.place(x=200, y=50)

    SearchPath = tk.Button(text="bestand zoeken", command=partial(ChoosenFunction, Path))
    SearchPath.place(x=400, y=200)



    



# connect to android device
def ConnectDevice(WhatToDo):
    global ssh
    global sftp

    WhatToDo = WhatToDo.get()
    IsNumber = WhatToDo.isnumeric()
    # checken of het ingevoerde getal een nummer is als dit wel zo is dan gaat het door anders dan krijg je een foutmelding
    if IsNumber == True:
        # controleren of het ingevoerde getal tussen de 1 en de 4 zit als dit wel het geval is ga het door anders dan krijg je een foutmelding
        if int(WhatToDo) > 0 and int(WhatToDo) < 5:
            # proberen of hij kan verbinden als hij het wel kan dan verbind hij en als hij het niet kan krijg je een foutmelding te zien
            try:
                print ("Starting connection")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port)
                sftp = ssh.open_sftp()
                print ("Connected.")

                if WhatToDo == "1":
                    # Bestand in de tablet zoeken (in dit geval een foto)
                    print ("foto zoeken")
                    Foto = list()
                    filePath = "/storage/emulated/0/Download"
                    FilePattern = '"*.png"'
                    rawcommand = "find {path} -name {pattern}"
                    command = rawcommand.format(path=filePath, pattern=FilePattern)


                    stdin, stdout, stderr = ssh.exec_command(command)
                    filelist = stdout.read().splitlines()


                    for afile in filelist:
                        (head, filename) = os.path.split(afile)
                        Foto.append(filename)

                    print (Foto)


                elif WhatToDo == "2":
                    # bestand in de tablet verwijderen in dit geval "testweg.png"
                    # sftp.remove("/storage/emulated/0/Download/testweg.png")
                    AskPath(DeleteFile)
                    # print ("file has been removed")

                elif WhatToDo == "3":
                    # bestand vanaf de pi naar de tablet toe sturen
                    # sftp.put("/home/mike/test/testfile.txt", "/storage/emulated/0/Download/testfile.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
                    # print ("The file has been transfered to your device")
                    AskPath(SendFile)

                else:
                    # bestand van de tablet naar de pi sturen
                    # sftp.get("/storage/emulated/0/Download/terugsturen.txt", "/home/mike/test/terugsturen.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
                    # print ("the file has been downloaded")
                    AskPath(ReceiveFile)

            except:
                showerror("","Kan niet verbinden")
        else:
            showerror("", "Het getal moet tussen de 1 en te 4 zijn")
    else:
        showerror("", "Je moet een getal invullen")

def Disconnect():
    # end script
    try:
        sftp.close()

        ssh.close()
        print ("Verbinding verbroken")

        time.sleep(2)
        window.destroy()
    except:
        showerror("", "Kan verbinding niet verbreken")


def StartWindow():
    global AskWhatToDo
    global Textbox
    global ConnectButton
    # window aanmaken en de buttons en invoerbalk aanmaken
    Choise = tk.StringVar()
    AskWhatToDo = tk.Label(window, background="lightgrey", text="Wat wilt u doen? 1). Bestand(en) zoeken \n2). Bestand verwijderen \n3). Bestand Sturen \n4). Bestand Ophalen ")
    AskWhatToDo.place(x=200, y=30)

    Textbox = tk.Entry(window, width=30, textvariable=Choise)
    Textbox.place(x=200, y=110)

    ConnectButton = tk.Button(text="Verbind met apparaat", command=partial(ConnectDevice, Choise))
    ConnectButton.place(x=400, y=200)

    DisconnectButton = tk.Button(text="Verbeek verbinding", command=Disconnect)
    DisconnectButton.place(x=100, y=200)

StartWindow()








# Here you will add all scripts you need to run






# # end script
# sftp.close()

# ssh.close()

window.mainloop()