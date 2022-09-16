from PIL import Image
from os.path import exists
import tkinter as tk
from functools import partial
from tkinter.messagebox import showerror


# /home/mike/test/testfile --tekstbestand
# /home/mike/test/testfoto -- fotobestand




# checken of het een echt bestand is en het bestand openen
def FileSearch(NameFile, Text_Image):
    NameFile = NameFile.get()
    Text_Image = Text_Image.get()
    # Als alles aan de eisen voldoet dan word het bestand geopent
    if (Text_Image == "1" or Text_Image == "2") and len(NameFile) >= 1:
        CheckFile = exists(NameFile)
        if CheckFile == True:
            if Text_Image == "1":
                OpenImage = Image.open(NameFile)
                OpenImage.show()
            else:
                FileOpen = open(NameFile)
                print (FileOpen.read())
        else:
            print("dit is geen geldig pad of bestand")
    # Als niet alles aan de eisen voldoet dan krijg je een melding te zien dat het niet goed is.
    elif int(Text_Image) >= 3:
        showerror("", "het getal moet kleiner dan 3 zijn")
    else:
        showerror("","Vul beide regels in om door te gaan.")



# window aanmaken
window = tk.Tk()
window.geometry("600x400")
window.title("File Searcher")
window.configure(background="lightgrey")


# vragen in de window zetten en de balken om de vragen te beantwoorden
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

    TextOrImage = tk.StringVar(value=0)

    QuestionLabel = tk.Label(window, background="lightgrey",text="Is het bestand een tekst of een foto? 1).foto / 2.tekst. ")
    QuestionLabel.place(x=200, y=100)
    # textbox om in te vullen of het een foto of een tekstbestand is
    TextBox2 = tk.Entry(window, width=30, textvariable=TextOrImage)
    TextBox2.place(x=200, y=120)

    # knop die doorverwijst naar de volgende functie om te controleren of de informatie klopt
    OpenFileButton= tk.Button(text="Bestand openen", command=partial(FileSearch, FileName, TextOrImage))
    OpenFileButton.place(x=230, y=200)

   

CreateWindow()



window.mainloop()