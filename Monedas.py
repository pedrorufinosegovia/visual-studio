from tkinter import *
from tkinter import ttk
class Convertidor(ttk.Frame):
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=229, width=378)
        self.inQuantity = ttk.Entry(self, font= ("Helvetica", 18, "bold"), width=10).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5,).place(x=38, y=71)
        ttk.Label(self, text="⥮").place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5).place(x=38, y=120)
        self.ootQuantity = ttk.Label(self, text="0000000000",width=10, font=("Helvetica", 18, "bold")).place(x=38, y=166)

class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("378x229")
        self.title("Cambio de Monedas")
        self.convertidor = Convertidor(self).place(x=0, y=0)
    def start(self):
        self.mainloop()

if __name__ == "__main__":
    begin = Mainapp()
    begin.start()