import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class NegativeValueError(Exception):
    pass

def check_negative(value):
    if value < 0:
        raise NegativeValueError("El valor ingresado debe ser mayor a 0")

def check_zero(value):
    if value == 0:
        raise ZeroDivisionError("El valor ingresado debe ser distinto de 0")

def distancia_MRU(v, t):
    check_negative(t)
    return v * t

def velocidad_MRU(d, t):
    check_negative(t)
    check_zero(t)
    return d / t

def tiempo_MRU(d, v):
    check_zero(v)
    return abs(d / v)

def distancia_MRUV(vi, t, a):
    check_negative(t)
    return vi * t + a * t ** 2 / 2

def velocidad_MRUV(vi, t, a):
    check_negative(t)
    return vi + a * t

def draw(vi, t, a):
    check_zero(t)
    check_negative(t)
    paso = t / 10
    tiempos = np.arange(0, t + paso, paso)
    x = [distancia_MRUV(vi, i, a) for i in tiempos]
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(tiempos, x)
    ax.set_title("Δx en función del tiempo")
    ax.set_xlabel("Tiempo (segundos)")
    ax.set_ylabel("Distancia (metros)")

    plot_frame = ttk.Frame(root)
    plot_frame.grid(row=17, column=0, columnspan=2, padx=10, pady=10)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def calcular():
    try:
        if opcion.get() == "MRU":
            tipo_calculo = tipo_calculo_mru.get()
            if tipo_calculo == "Distancia (Δx)":
                v = float(v_entry.get())
                t = float(t_entry.get())
                resultado = distancia_MRU(v, t)
                messagebox.showinfo("Resultado", f"Distancia (Δx): {resultado:.2f} m")