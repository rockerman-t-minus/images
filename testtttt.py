from tkinter import *
from PIL import Image, ImageTk

root = Tk()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

e = Entry(root, width=50, bg='light blue', borderwidth=3)
e.pack()
e.insert(0, '')

my_label = Label()
my_label.pack()


def myClick():
    link = r'' + e.get()
    my_img = ImageTk.PhotoImage(Image.open(link))
    my_label.configure(image=my_img)
    my_label.image = my_img


myButton = Button(root, text='Scan Part Number', command=myClick,
                  bg='pink', fg='white')
myButton.pack()

root.mainloop()
