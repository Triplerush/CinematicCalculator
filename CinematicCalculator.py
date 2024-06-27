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
