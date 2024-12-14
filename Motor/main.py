from tkinter import Tk, Label, Canvas, messagebox
from PIL import Image, ImageTk
from time import strftime

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Control de Motor")
ventana.iconbitmap("img/motordetenido.ico")
titulo = Label(ventana, text="Control Motor", font=("Arial", 20, "bold"))
titulo.pack()


ventana.mainloop()