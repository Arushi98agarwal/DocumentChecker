from tkinter import *
from pycode_similar import *

txt=None
txt1=None
lbl=None
def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text=res)
    global txt
    global txt1
    global lbl
    text1 = open(txt.get(),"rb")
    text2 = open(txt1.get(),"rb")

    
    result=main(text1,text2)
    lbl.configure(text=str(result))

def pySimilar():
    window = Tk()
    window.title("Degree of Similarity in Python Code Files")
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
    global txt
    global txt1
    global lbl
    lbl = Label(window, text="Degree of Similarity between Two Python Code Files",font=("Arial Bold", 10))
    lbl.grid(column=6, row=5)

    txt = Entry(window,width=40)
    txt.grid(column=6, row=7,columnspan=2)

    txt1 = Entry(window,width=40)
    txt1.grid(column=6, row=8,columnspan=2)
    
    btn = Button(window, text="Click Me",bg="orange", fg="red",command=clicked)
    btn.grid(column=6, row=9)

    window.mainloop()

