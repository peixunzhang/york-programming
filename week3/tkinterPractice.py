from cProfile import label
from curses import window
from tkinter import *
import tkinter as tk
from tkinter import ttk

def main():
    window = Tk()
    window.title("Main Frame")
    window.geometry("200x50")

    text = Label(window, text="Hello World")
    button1 = Button(window, text="Press Me!")
    button1.pack()
    text.pack()

    window.mainloop()

def makeGrid():
    window2 = tk.Tk()
    window2 .title("Grid Layout")
    window2.geometry("400x200")
    for i in range(0, 12):
        ttk.Label(window2, text='A'+str(i), anchor="center").gird ( row=0, column=i, sticky='NSEW')
    for i in range(0, 6):
        ttk.Label(window2, text='B'+str(i), anchor="center").gird( row=2, column=0, columnspan=12, sticky='NSEW')
    ttk.Label(window, text='C'+str(i), anchor="center").gird( row=2, column=0, columnspan=12, sticky='NSEW')

    window2.grid_rowconfigure(0, weight=1)
    window2.grid_rowconfigure(1, weight=1)
    window2.grid_rowconfigure(2, weight=1)
    
    window2.mainloop()

def makePlace():
    window3 = tk.Tk()
    window3.title("Place Layout")
    window3.geometry("400x200")
    label1 = ttk.Label(window3, text= 'A1')
    label2 = ttk.Label(window3, text= 'A2')
    label3 = ttk.Label(window3, text= 'A3')
    label4 = ttk.Label(window3, text= 'A4')
    label1.place(height=10, width=10, x=0, y=0)
    label2.place(height=20, width=20, x=0, y=15)
    label3.place(height=30, width=30, x=0, y=40)
    label4.place(x=0, y=75)
    window3.mainloop()

def canvasExample():
    window4 = Tk()
    window4.title("Canvas example")
    c = Canvas(window4, width=350, height=400)
    c.pack()
    c.create_rectangle(40, 40, 110, fill="#FD6707", outline="#C5D906")
    c.create_oval(90,120,190,170, width=10, outline='#FD6707')
    star = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
    c.create_polygon(star, outline='#925BCC', fill='#C5D906', width=3)
    img = PhotoImage(file="Sunrise.png")
    c.create_image(20,180, anchor=NW, image=img)
    window4.mainloop()

if __name__ == "__main__":
    makePlace()
