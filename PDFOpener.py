from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Button
import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
import os
from tkinter.messagebox import showerror
from functools import partial
import pdfplumber


class ShowPdf(pdf.ShowPdf):
    def goto(self, page):
        page = page.get()
        CheckNumber = page.isdigit()
        
        if CheckNumber == True:
            with pdfplumber.open(filename) as OpenedPDF:
                TotalPages = len(OpenedPDF.pages)
                print (TotalPages)

                if int(page) <= TotalPages:
                    if int(page) > 0:
                        try:
                            self.text.see(self.img_object_li[int(page) - 1])
                        except IndexError:
                            if self.img_object_li:
                                self.text.see(self.img_object_li[-1])
                    else:
                        showerror("", "Page 0 does not exist")
                else:
                    showerror("", "Page number is to high")
        else:
            showerror("", "Please fill in a number")





SearchResults = None

# window aanmaken
root = tk.Tk()
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
# root.geometry("900x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")





# PageNumbers = []

# main part of program

def PDFDestroy(PDF, XButton):
    PDF.destroy()
    SearchBar.destroy()
    SearchButton.destroy()
    SearchResults.destroy()
    XButton.destroy()
    # filename = None
    





# Hier wordt een rode X knop aangemaakt om de file te sluiten.
def X_Button(PDF):
    Destroy_Button = tk.Button(root, text="X", bg="red", fg="white", height=1, command=partial(PDFDestroy, PDF))
    Destroy_Button.place(x=1530, y=20)
    Destroy_Button.config(command=partial (PDFDestroy, PDF, Destroy_Button))






# hier wordt de file explorer geopent waar je kan kiezen welke pdf je wilt openen, daarna wordt hij hier ook geopent om te laten zien.

def browseFiles():
    global filename
    global v2
    global v1

    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file", filetypes=(("PDF File", ".pdf"), ("PDF File", ".PDF"), ("All file", ".txt")))
    v1 = ShowPdf()
    # print (v1)
    v2 = v1.pdf_view(root, pdf_location=open(filename, "r"), width=150, height=100)
    v2.pack(pady=(0,0))

    X_Button(v2)




# tekst "type to search" wordt in de zoekbalk verwijderd zodra je erop klikt
def TempTextSearchBar(e):
    SearchBar.delete(0, "end")
    



# hier worden de pagina nummers van waar het gezochte woord gevonden is getoond
def ShowSearchResults(Results = "", NumberPages = 0):
    global SearchResults
    Results = list(Results)
    Results.sort()
    Counter = 0
    NewPagesList = []
    NumberNewLines = NumberPages / 5
    SearchResults = tk.Label(root , height=49,width=21 ,bg="white", anchor=NW)
    SearchResults.place(x=157 , y=180)
    if NumberPages > 0:
        SearchResults.config(bg="lightgrey")
        if NumberNewLines >= 1:
            for i in Results:
                NewPagesList.append(i)
                Counter += 1
                if Counter == 5:
                    NewPagesList.append('\n')
                    Counter = 0
            Results = NewPagesList
        SearchResults.config(text=Results)

    

    











# hier wordt gezocht naar het ingevoerde woord hij gaat elke pagina af en hij houdt bij op welke hij hem gevonden heeft, En hij telt op hoeveel pagina's het woord wordt gevonden
# Als het woord 2 keer op 1 pagina gevonden wordt wordt het maar 1 keer getoond
def SearchAction(SearchVariable):
    PageNumbers = []
    Counter = 0
    SearchWord = SearchVariable.get()
    with pdfplumber.open(filename) as OpenedPDF:
        TotalPages = len(OpenedPDF.pages)

        for i in range (TotalPages):
            print (i)
            page = OpenedPDF.pages[i]
            PageText = page.extract_text()
            if SearchWord != "":
                if SearchWord in PageText:
                    PageNumbers.append(i + 1)
                    Counter += 1

                    
        if PageNumbers == []:
            showerror("", "Does not match with anything in this file")
        else:
            ShowSearchResults(set(PageNumbers), Counter)
        

	




# Hier wordt de invoerbalk en knop gemaakt om een bepaald woord te zoeken
def CreateSearchBar():
    global SearchBar
    global SearchButton
    SearchVariable = tk.StringVar()
    SearchBar = tk.Entry(root, textvariable=SearchVariable)
    SearchBar.insert(0, "Type to search")
    SearchBar.place(x=160, y=120)

    SearchBar.bind("<FocusIn>", TempTextSearchBar)

    SearchButton = tk.Button(root, text="Search", command=partial(SearchAction, SearchVariable))
    SearchButton.place(x=160, y=150)



def TempTextPageBar(e):
    PageBar.delete(0, "end")



# Hier wordt de invoerbalk en knop gemaakt om naar een bepaalde pagina te gaan
def CreatePageBar():
    global PageBar

    PageVariable = tk.StringVar()

    PageBar = tk.Entry(root, textvariable=PageVariable)
    PageBar.insert(0, "Type to search")
    PageBar.place(x=1570, y=120)

    PageBar.bind("<FocusIn>", TempTextPageBar)


    PageButton = tk.Button(root, text="Search Page", command=lambda: [v1.goto(PageVariable)])
    PageButton.place(x=1570, y=150)






# Hier wordt de button gemaakt die je meteen in het begin ziet om de file explorer te openen
PdfOpenButton = tk.Button(root, text="open", command=lambda: [browseFiles(), CreateSearchBar(), ShowSearchResults(), CreatePageBar()],width=40,font="arial 20", bd=4).pack()

root.mainloop()