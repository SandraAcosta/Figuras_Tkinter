# -*- coding: utf-8 -*-
from Tkinter import *
from Figuras import *
from Circulo import *
from Cuadrado import *
from Puntos import *
from Rectangulo import *
from Triangulo import *

import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")
    
def prueba():
    print("Se ha elegido la opcion" + variable.get())

def CalculoArea ():
    opc = variable.get()
    p = Punto()
    q = Punto()
    p.x = txtx1.get()
    p.y = txty1.get()
    q.x = txtx2.get()
    q.y = txty2.get()
    if opc == "1":
        f=Rectangulo()
    elif opc == "2":
        f=Triangulo()
    elif opc == "3":
        f=Circulo()
    elif opc == "4":
        f=Cuadrado()
    f.setPuntos(p, q)
    f.calculararea()
    etiqueta7 = tk.Label(root, text="El área es "+ str(f.area))
    etiqueta7.pack()

def CalculoPerimetro():
    opc = variable.get()
    p = Punto()
    q = Punto()
    p.x = txtx1.get()
    p.y = txty1.get()
    q.x = txtx2.get()
    q.y = txty2.get()
    if opc == "1":
        f=Rectangulo()
    elif opc == "2":
        f=Triangulo()
    elif opc == "3":
        f=Circulo()
    elif opc == "4":
        f=Cuadrado()
    f.setPuntos(p, q)
    f.calcularperimetro()
    etiqueta7 = tk.Label(root, text="El perímetro es "+ str(f.perimetro))
    etiqueta7.pack()

     
root = tk.Tk()
root.title("Cálculo de Áreas y Perímetros")
root.geometry('400x500')
etiqueta1 = tk.Label(root, text="Ingrese coordenada x del punto 1")
etiqueta1.pack()
txtx1 = tk.IntVar(root)
P1_x = tk.Entry(root, textvariable = txtx1)
P1_x.pack()
etiqueta2 = tk.Label(root, text="Ingrese coordenada y del punto 1")
etiqueta2.pack()
txty1 = tk.IntVar(root)
P1_y = tk.Entry(root, textvariable = txty1)
P1_y.pack()
etiqueta3 = tk.Label(root, text="Ingrese coordenada x del punto 2")
etiqueta3.pack()
txtx2 = tk.IntVar(root)
P2_x = tk.Entry(root, textvariable = txtx2)
P2_x.pack()
etiqueta4 = tk.Label(root, text="Ingrese coordenada y del punto 2")
etiqueta4.pack()
txty2 = tk.IntVar(root)
P2_y = tk.Entry(root, textvariable = txty2)
P2_y.pack()


etiqueta5 = tk.Label(root, text="Elija la figura o figuras")
etiqueta5.pack()
variable = tk.StringVar()
radiobutton1 = tk.Radiobutton(text="Rectangulo", variable=variable, value=1, command=prueba)
radiobutton2 = tk.Radiobutton(text="Triangulo", variable=variable, value=2, command=prueba)
radiobutton3 = tk.Radiobutton(text="Circulo", variable=variable, value=3, command=prueba)
radiobutton4 = tk.Radiobutton(text="Cuadrado", variable=variable, value=4, command=prueba)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

etiqueta6 = tk.Label(root, text="Elija Calcular Area o Perimetro")
etiqueta6.pack()

botonArea = tk.Button(root, text="Calcular Area", command=CalculoArea)
botonArea.pack()
botonPerimetro = tk.Button(root, text="Calcular Perimetro", command=CalculoPerimetro)
botonPerimetro.pack()

root.mainloop()
