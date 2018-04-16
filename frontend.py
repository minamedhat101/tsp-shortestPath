from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backend

def tsp():
  tspStr= backend.travillingsalesMan()
  messagebox.showinfo("To travel to all bulidings",tspStr)

def short():
  shortestPathStr = backend.shortsPath(fromText.get(), toText.get())
  messagebox.showinfo("The Shortest path is",shortestPathStr)

window=Tk()

window.wm_title("maps")

img = ImageTk.PhotoImage(Image.open("map2.jpg"))
labelImage = Label(window, image = img)
labelImage.pack(side = "bottom")

Button(window,text="Traveling Salesman", width=15, command=tsp).pack(padx=0, pady=5,side ="bottom") 

Label(window,text="From").pack(padx=3, pady=0, side ="left")

fromText=StringVar()
Entry(window,textvariable=fromText).pack(padx=3, pady=5,side ="left")

Label(window,text="To").pack(padx=3, pady=10,side ="left")

toText=StringVar()
Entry(window,textvariable=toText).pack(padx=3, pady=15,side ="left")

Button(window,text="Shortest Path", width=15, command=short).pack(padx=3, pady=15,side ="left")

window.mainloop()