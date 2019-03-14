from tkinter import *
from tkinter import ttk
import requests
currencies= {"EUR": 1, "USD": 0.9, "CAD": 0.75}

class Convertidor(ttk.Frame):
    __APYCURRENCYLIST_EP =  "https://free.currencyconverterapi.com/api/v6/currencies"
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=229, width=378)
        #Variables de Control
        self.inQuantity = DoubleVar(value=0)
        self.__strinQuantity = StringVar(value="")
        self.__oldvalueinQuantity = ""
        self.__strinQuantity.trace("w", self.validateQuantity)
        self.outQuantity = 0.0
        self.inCurrency = StringVar()
        self.outCurrency = StringVar()
        currencieskey=[]
        for keys in currencies:
            currencieskey.append(keys)
        self.inQuantityEntry = ttk.Entry(self, font= ("Helvetica", 18, "bold"), width=10, textvariable=self.__strinQuantity).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5,values=currencieskey, textvariable=self.inCurrency)
        self.inCurrencyCombo.place(x=38, y=71)
        self.inCurrencyCombo.bind("<<ComboboxSelected>>", self.Convertirdivisas)
        ttk.Label(self, text="⥮").place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5,values=currencieskey,textvariable=self.outCurrency)
        self.outCurrencyCombo.place(x=38, y=120)
        self.outCurrencyCombo.bind("<<ComboboxSelected>>", self.Convertirdivisas)
        self.outQuantityLabel = ttk.Label(self, text="",width=10, font=("Helvetica", 18, "bold"))
        self.outQuantityLabel.place(x=38, y=166)

    def Convertirdivisas(self, *args):
        _amount = (self.__strinQuantity.get())
        _from = self.inCurrency.get()
        _to = self.outCurrency.get()
        resultado = "0"
        if _amount != "" and _from != "" and _to != "":
            resultado = float(_amount)* currencies[_from] / currencies[_to]
            self.outQuantityLabel.config(text=str(resultado))

    def validateQuantity(self, *args):
        try:
            if self.__strinQuantity.get() != "":
                v = self.__strinQuantity.get()
                if "-" in v:
                    self.__strinQuantity.set(self.__oldvalueinQuantity)
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
        self.convertidor = Convertidor(self)
        self.convertidor.place(x=0, y=0)
    def start(self):
        self.mainloop()

if __name__ == "__main__":
    begin = Mainapp()
    begin.start()