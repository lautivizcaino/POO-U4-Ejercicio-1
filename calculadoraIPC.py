import tkinter as tk
from tkinter import ttk,messagebox
import math
class Calculadora(tk.Tk):
    __cantidadVest=None
    __precioBaseVest=None
    __precioActualVest=None
    __cantidadAli=None
    __precioBaseAli=None
    __precioActualAli=None
    __cantidadEdu=None
    __precioBaseEdu=None
    __precioActualEdu=None
    __ipc=None
    def __init__(self):
        super().__init__()
        self.title('Calculadora IPC')
        self.geometry('360x150')
        mainframe=ttk.Frame(self,padding='3 3 12 12')

        item=tk.Label(self,text='Item')
        item.grid(row=0,column=0,sticky='W')

        cantidad=tk.Label(self,text='Cantidad')
        cantidad.grid(row=0,column=1,sticky='W')

        precioBase=tk.Label(self,text='Precio Año Base')
        precioBase.grid(row=0,column=2,sticky='W')

        precioActual=tk.Label(self,text='Precio Año Actual')
        precioActual.grid(row=0,column=3,sticky='W')


        vestimenta=tk.Label(self,text='Vestimenta')
        vestimenta.grid(row=1,column=0,sticky='W')

        self.__cantidadVest=tk.StringVar()
        vestimentaCant=tk.Entry(self,textvariable=self.__cantidadVest,width=15)
        vestimentaCant.grid(row=1,column=1,sticky='W')

        self.__precioBaseVest=tk.StringVar()
        vestimentaPB=tk.Entry(self,textvariable=self.__precioBaseVest,width=15)
        vestimentaPB.grid(row=1,column=2,sticky='W')

        self.__precioActualVest=tk.StringVar()
        vestimentaPA=tk.Entry(self,textvariable=self.__precioActualVest,width=15)
        vestimentaPA.grid(row=1,column=3,sticky='W')

        alimentos=tk.Label(self,text='Alimentos')
        alimentos.grid(row=2,column=0,sticky='W')

        self.__cantidadAli=tk.StringVar()
        alimentosCant=tk.Entry(self,textvariable=self.__cantidadAli,width=15)
        alimentosCant.grid(row=2,column=1,sticky='W')

        self.__precioBaseAli=tk.StringVar()
        alimentosPB=tk.Entry(self,textvariable=self.__precioBaseAli,width=15)
        alimentosPB.grid(row=2,column=2,sticky='W')

        self.__precioActualAli=tk.StringVar()
        alimentosPA=tk.Entry(self,textvariable=self.__precioActualAli,width=15)
        alimentosPA.grid(row=2,column=3,sticky='W')

        educacion=tk.Label(self,text='Educacion')
        educacion.grid(row=3,column=0,sticky='W')

        self.__cantidadEdu=tk.StringVar()
        educacionCant=tk.Entry(self,textvariable=self.__cantidadEdu,width=15)
        educacionCant.grid(row=3,column=1,sticky='W')

        self.__precioBaseEdu=tk.StringVar()
        educacionPB=tk.Entry(self,textvariable=self.__precioBaseEdu,width=15)
        educacionPB.grid(row=3,column=2,sticky='W')

        self.__precioActualEdu=tk.StringVar()
        educacionPA=tk.Entry(self,textvariable=self.__precioActualEdu,width=15)
        educacionPA.grid(row=3,column=3,sticky='W')

        calcularIPC=tk.Button(self, text="Calcular IPC",padx=5,pady=5, command=self.calcular) 
        calcularIPC.grid(row=4,column=1)

        salir=tk.Button(self,text="Salir",padx=5,pady=5,command=quit)
        salir.grid(row=4,column=2,columnspan=2)

        
        ipc=tk.Label(self,text='IPC').grid(row=5,column=0)
        self.__ipc=tk.StringVar()
        ipcObtenido=tk.Label(self,textvariable=self.__ipc).grid(row=5,column=1,sticky='E')

        porcentaje=tk.Label(self,text='%').grid(row=5,column=2,sticky='W')

    def calcular(self):
        try:
            base=int(self.__cantidadVest.get())*float(self.__precioBaseVest.get())+int(self.__cantidadAli.get())*float(self.__precioBaseAli.get())+int(self.__cantidadEdu.get())*float(self.__precioBaseEdu.get())
            
            actual=int(self.__cantidadVest.get())*float(self.__precioActualVest.get())+int(self.__cantidadAli.get())*float(self.__precioActualAli.get())+int(self.__cantidadEdu.get())*float(self.__precioActualEdu.get())
            ipc=math.modf(actual/base)
            ipcPorcentual=ipc[0]*100
            self.__ipc.set(math.trunc(ipcPorcentual))
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')



