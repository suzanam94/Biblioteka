from Biblioteka import *
from tkinter import *

root = Tk()
root.title("Biblioteka")

l1 = Label(root, text = "Id clana")
l1.pack()

e1 = Entry(root)
e1.pack()

l2 = Label(root, text = "Id knjige")
l2.pack()

e2 = Entry(root)
e2.pack()

b1 = Button(root, text = "Uzmi knjigu", command = lambda:
            B.uzmi_knjigu(e1.get(), e2.get()))
            
b1.pack(side = LEFT)

b2 = Button(root, text = "Vrati knjigu", command = lambda:
        B.vrati_knjigu(e1.get(), e2.get()))
b2.pack(side = RIGHT)


mainloop()
