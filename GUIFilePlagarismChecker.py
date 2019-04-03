from tkinter import *
from difflib import SequenceMatcher
import PyPDF2

from docx import Document

lbl=None
txt=None
txt1=None

def clicked():
    global lbl
    global txt
    global txt1
    text1 = open(txt.get())
    text2 = open(txt1.get())

    file1_data = text1.read()
    file2_data = text2.read()

    
    #result=main(text1,text2)
    result=SequenceMatcher(None,file1_data,file2_data).ratio()
    lbl.configure(text=str(result*100))
def fileSimilar():
    global lbl
    global txt
    global txt1
    window = Tk()
    window.title("Plagarism Checking between two Files")
    window.geometry('450x300')

    mrg1=Label(window,text='')
    mrg1.grid(column=0, row=0)

    mrg2=Label(window,text='')
    mrg2.grid(column=1, row=1)

    mrg3=Label(window,text='')
    mrg3.grid(column=2, row=2)

    mrg4=Label(window,text='')
    mrg4.grid(column=3, row=3)

    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=4)

    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=6)

    lbl = Label(window, text="Plagarism Checking between two Files",font=("Arial Bold", 10))
 
    lbl.grid(column=6, row=5)

    txt = Entry(window,width=40)
 
    txt.grid(column=6, row=7,columnspan=2)

    txt1 = Entry(window,width=40)
 
    txt1.grid(column=6, row=8,columnspan=2)

    btn = Button(window, text="Click Me",bg="orange", fg="red",command=clicked)
 
    btn.grid(column=6, row=9)

 
    window.mainloop()

