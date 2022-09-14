# hier wordt alles geimporteerd wat er nodig is voor dit programma
from PIL import Image
from os.path import exists
import tkinter as tk
from functools import partial
from tkinter.messagebox import showerror
import os
import webbrowser

# test files om te werking te testen
# /home/mike/test/testfile.txt --tekstbestand
# /home/mike/test/testfoto.JPG -- fotobestand
# /home/mike/test/test.pdf -- test pdf bestand




# checken of het een echt bestand is en het bestand openen
def FileSearch(NameFile):
    NameFile = NameFile.get()
    # checken of er iets is ingevoerd
    if len(NameFile) >= 1:
        # kijken of het pad en bestand bestaan
        CheckFile = exists(NameFile)
        if CheckFile == True:
            Extension = os.path.splitext(NameFile)
            # Hier word gekeken naar de extensie van het bestand en word vergeleken
            # en als deze klopt word hij geopent en als deze bij geen een klopt krijg je een melding dat dit niet kan worden geopent
            try:
                if Extension[1] == ".txt":
                    FileOpen = open(NameFile)
                    print (FileOpen.read())
                elif Extension[1] == ".png" or Extension[1] == ".jpg":
                    print ("test")
                    OpenImage = Image.open(NameFile)
                    OpenImage.show()
                elif Extension[1] == ".pdf":
                    webbrowser.open_new(NameFile)
                else:
                    showerror("", "Dit soort type bestand kan niet geopent worden. ")
                  
            # Als er geen bestand is ingevoerd dan word er een error gegeven
            except IsADirectoryError:
                showerror("", "Dit is een pad, vul ook een bestand in.")
        # Als het bestand of pad niet geldig is dan word er hier een error gegeven
        else:
            showerror("", "Dit is geen geldig pad of bestand.")
    # Als er niets is is ingevoerd dan word er hier een error gegeven en wordt er gezegd dat er dat je iets moet invullen
    else:
        showerror("","Vul iets in om door te gaan.")



# window aanmaken
window = tk.Tk()
window.geometry("600x400")
window.title("File Searcher")
window.configure(background="lightgrey")


#  knop en invulbalk maken
def CreateWindow():
    FileName = tk.StringVar()
    Window1 = tk.Label(window,
        background="lightgrey",
        text="Voer het pad van het bestand in."
    )
    Window1.place(x=200, y=30)
    # textbox om het pad en bestand in te vullen
    TextBox = tk.Entry(window, width = 30, textvariable=FileName)
    TextBox.place(x=200, y=50)


    # knop die doorverwijst naar de volgende functie om te controleren of de informatie klopt
    OpenFileButton= tk.Button(text="Bestand openen", command=partial(FileSearch, FileName))
    OpenFileButton.place(x=230, y=200)

   

CreateWindow()



window.mainloop()