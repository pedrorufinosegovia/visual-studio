from tkinter import *
from tkinter import ttk
class Imputs(ttk.Frame):
    def __init__(self, parent, **args):
        ttk.Frame__init__
class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("378x229")
        self.title("Cambio de Monedas")
    def start(self):
        self.mainloop()

if __name__ == "__main__":
    begin = Mainapp()
    begin.start()