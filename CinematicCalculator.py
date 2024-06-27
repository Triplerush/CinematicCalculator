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
            elif tipo_calculo == "Velocidad (v)":
                d = float(d_entry.get())
                t = float(t_entry.get())
                resultado = velocidad_MRU(d, t)
                messagebox.showinfo("Resultado", f"Velocidad (v): {resultado:.2f} m/s")
            elif tipo_calculo == "Tiempo (Δt)":
                d = float(d_entry.get())
                v = float(v_entry.get())
                resultado = tiempo_MRU(d, v)
                messagebox.showinfo("Resultado", f"Tiempo (Δt): {resultado:.2f} s")
        elif opcion.get() == "MRUV":
            tipo_calculo = tipo_calculo_mruv.get()
            vi = float(vi_entry.get())
            t = float(t_entry.get())
            a = float(a_entry.get())
            if tipo_calculo == "Distancia (Δx)":
                resultado = distancia_MRUV(vi, t, a)
                messagebox.showinfo("Resultado", f"Distancia (Δx): {resultado:.2f} m")
            elif tipo_calculo == "Velocidad final (Vf)":
                resultado = velocidad_MRUV(vi, t, a)
                messagebox.showinfo("Resultado", f"Velocidad final (Vf): {resultado:.2f} m/s")
            elif tipo_calculo == "Gráfica de Δx en función de Δt":
                draw(vi, t, a)
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    except NegativeValueError as e:
        messagebox.showerror("Error", str(e))
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Ecuaciones de MRU y MRUV")
