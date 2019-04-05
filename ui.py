from tkinter import*

window = Tk()
window.title("ksdasndsnadn")

bg_image = PhotoImage(file ="ui.jpeg")
x = Label (image = bg_image)
x.grid(row = 0, column = 0)


window.geometry("600x300")
app = Application(window)
window.mainloop()

