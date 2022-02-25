from tkinter import Tk, Button, Label
from people import queue


window = Tk()
window.title('Фанты')

lbls = [Label(window, text=queue[0], height=1, width=20) for i in range(20)]
for i, lbl in enumerate(lbls):
    lbl.grid(column=0, row=i)
    lbl.config(font=('Courier', 44))
i = 0


def build_labels():
    global i
    for j, lbl_ in enumerate(lbls):
        lbl_.configure(text=queue[(i + j) % len(queue)])
        if j == 0:
            lbl_.configure(fg='red')
    i += 1


button = Button(window, text='Следующий', command=build_labels)
button.grid(column=2, row=0)
button.config(font=('Courier', 44))
window.geometry('1920x1080')

window.mainloop()
