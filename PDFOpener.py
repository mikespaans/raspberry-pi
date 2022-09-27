from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
import os
from tkinter.messagebox import showerror
from functools import partial
import pdfplumber

# instalizing tk
root = tk.Tk()
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
# root.geometry("900x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")


# PageNumbers = []

# main part of program

def browseFiles():
    global filename
    global v2
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file", filetypes=(("PDF File", ".pdf"), ("PDF File", ".PDF"), ("All file", ".txt")))
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(root, pdf_location=open(filename, "r"), width=150, height=100)
    v2.pack(pady=(0,0))
    # pdfplumber.open(filename)


def TempText(e):
    SearchBar.delete(0, "end")
    

def ShowSearchResults(Results, NumberPages):
    Results = list(Results)
    Results.sort()
    Counter = 0
    NewPagesList = []
    NumberNewLines = NumberPages / 5
    if NumberNewLines >= 1:
        for i in Results:
            NewPagesList.append(i)
            Counter += 1
            if Counter == 5:
                NewPagesList.append('\n')
                Counter = 0
        Results = NewPagesList

    SearchResults = tk.Label(root,text=Results , height=49,width=21 ,bg="lightgrey", anchor=NW)
    SearchResults.place(x=159, y=180)


# TestList = [1,2,4,4,5,6,7,78,8,2,4,6,4,4,4,4,4]
# ShowSearchResults(TestList, 17)




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
            showerror("", "Komt niet overeen met iets uit dit bestand")
        else:
            ShowSearchResults(set(PageNumbers), Counter)
        

	





def CreateSearchBar():
    global SearchBar
    SearchVariable = tk.StringVar()
    SearchBar = tk.Entry(root, textvariable=SearchVariable)
    SearchBar.insert(0, "Type to search")
    SearchBar.place(x=160, y=120)

    SearchBar.bind("<FocusIn>", TempText)

    SearchButton = tk.Button(root, text="Search", command=partial(SearchAction, SearchVariable))
    SearchButton.place(x=160, y=150)





# CreateSearchBar()


PdfOpenButton = tk.Button(root, text="open", command=lambda: [browseFiles(), CreateSearchBar()],width=40,font="arial 20", bd=4).pack()

root.mainloop()