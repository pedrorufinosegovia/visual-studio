from tkinter import *
from tkinter import ttk
currencies= {"EUR": 1, "USD": 0.9, "CAD": 0.75}

class Convertidor(ttk.Frame):
    __oldvalueinQuantity = None
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=229, width=378)
        #Variables de Control
        self.inQuantity = DoubleVar(value=0)
        self.__strinQuantity = StringVar(value="")
        self.__oldvalueinQuantity = ""
        self.__strinQuantity.trace("w", self.validateQuantity)
        self.outQuantity = 0.0
        self.inCurrency = StringVar()
        self.inCurrency.trace("w", self.Convertirdivisas)
        self.outCurrency = StringVar()
        self.outCurrency.trace("w", self.Convertirdivisas)
        currencieskey=[]
        for keys in currencies:
            currencieskey.append(keys)
        self.inQuantityEntry = ttk.Entry(self, font= ("Helvetica", 18, "bold"), width=10, textvariable=self.__strinQuantity).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5,values=currencieskey, textvariable=self.inCurrency).place(x=38, y=71)
        ttk.Label(self, text="⥮").place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5,values=currencieskey,textvariable=self.outCurrency).place(x=38, y=120)
        self.outQuantityLabel = ttk.Label(self, text="0000000000",width=10, font=("Helvetica", 18, "bold")).place(x=38, y=166)

    def Convertirdivisas(self):
        _amount = (self.__strinQuantity.get())
        _from = self.inCurrency.get()
        _to = self.outCurrency.get()
        resultado = "0"
        if _amount != "" and _from != "" and _to != "":
            if _to == "EUR":
                resultado = float(_amount)* currencies[_from]
            elif _from == "EUR":
                resultado = float(_amount)* currencies[_to]
            else:
                resultado = float(_amount)* currencies[_from] / currencies[_to]
            self.outQuantityLabel.config(text=str(resultado))

    def validateQuantity(self, *args):
        try:
            if self.__strinQuantity.get() != "":
                v = self.__strinQuantity.get()
                v = v.replace(".", "@")
                v = v.replace(",", ".")
                float(v)
                self.__oldvalueinQuantity = self.__strinQuantity.get()
                self.Convetirdivisas()
        except:
            self.__strinQuantity.set(self.__oldvalueinQuantity)

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