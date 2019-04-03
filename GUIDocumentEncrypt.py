from tkinter import *
import PyPDF2

txt=None
txt1=None
lbl=None

def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text=res)
    global txt
    global txt1
    global lbl
    
    password = txt1.get()
    text1=txt.get()
    pdfFile = open(text1, 'rb')

    # Create reader and writer object
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    # Add all pages to writer (accepted answer results into blank pages)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    # Encrypt with your password
    pdfWriter.encrypt(password)

    # Write it to an output file. (you can delete unencrypted version now)
    resultPdf = open('encrypted_output.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

    #result=main(text1,text2)
    lbl.configure(text="File Encrypted Successfully")

def fileEncrypt():
    window = Tk()
    window.title("Document Locker")
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
    lbl = Label(window, text="Enter PDF File Path and Password",font=("Arial Bold", 10))
    lbl.grid(column=6, row=5)

    txt = Entry(window,width=40)
    txt.grid(column=6, row=7,columnspan=2)

    txt1 = Entry(window,width=40)
    txt1.grid(column=6, row=8,columnspan=2)
    
    btn = Button(window, text="Click Me",bg="orange", fg="red",command=clicked)
    btn.grid(column=6, row=9)

    window.mainloop()

