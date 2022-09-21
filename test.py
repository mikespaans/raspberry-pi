# import subprocess

# # subprocess.Popen(["/home/mike/test/test.pdf"], shell=True)

# subprocess.call(["xdg-open", "/home/mike/Downloads/TestTekening.pdf"])




# import module


# # import os
# from pdf2image import convert_from_path

# # os.system("sudo mkdir Afbeeldingen")

# # Store Pdf with convert_from_path function
# images = convert_from_path('/home/mike/Downloads/TestTekening.pdf')

# # for i in range(len(images)):
# for i in range (1):

# 	# Save pages as images in the pdf
# 	images[i].save("Afbeeldingen/page"+ str(i) +'.jpg', 'JPEG')

# print ("klaar")



from tkinter import *
from tkinter import dialog
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

# instalizing tk
root = Tk()
root.geometry("630x700+400+100")
root.title("PDF viewer")
root.configure(bg="white")


# main part of program

def browseFiles():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file", filetypes=(("PDF File", ".pdf"), ("PDF File", ".PDF"), ("All file", ".txt")))
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(root, pdf_location=open(filename, "r"), width=77, height=100)
    v2.pack(pady=(0,0))
    





Button(root, text="open", command=browseFiles,width=40,font="arial 20", bd=4).pack()

root.mainloop()