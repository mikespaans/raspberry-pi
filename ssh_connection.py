import paramiko
import os

host = "192.168.1.102"
port = 2222
# username = "Lenovo Tab M10 FHD Plus"
# password = "password"


# connect to android device
print ("Starting connection")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port)
sftp = ssh.open_sftp()
print ("Connected.")




# Here you will add all scripts you need to run


# # Bestand in de tablet zoeken (in dit geval een foto)
# print ("foto zoeken")
# Foto = list()
# filePath = "/storage/emulated/0/Download"
# FilePattern = '"*.png"'
# rawcommand = "find {path} -name {pattern}"
# command = rawcommand.format(path=filePath, pattern=FilePattern)


# stdin, stdout, stderr = ssh.exec_command(command)
# filelist = stdout.read().splitlines()


# for afile in filelist:
#     (head, filename) = os.path.split(afile)
#     Foto.append(filename)

# print (Foto)



# # bestand in de tablet verwijderen in dit geval "testweg.png"
# sftp.remove("/storage/emulated/0/Download/testweg.png")
# print ("file has been removed")



# # bestand vanaf de pi naar de tablet toe sturen
# sftp.put("/home/mike/test/testfile.txt", "/storage/emulated/0/Download/testfile.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
# print ("The file has been transfered to your device")


# # bestand van de tablet naar de pi sturen
# sftp.get("/storage/emulated/0/Download/terugsturen.txt", "/home/mike/test/terugsturen.txt") #je moet de naam van het bestand opnieuw typen in de bestemming
# print ("the file has been downloaded")





# end script
sftp.close()

ssh.close()