import tkinter as tk
from tkinter import messagebox
from indexed_sequential_search import *
import os


def search(ascending=True):
    elements_list = entry_elements.get()
    block_size = int(entry_block_size.get())
    target = int(entry_target.get())

    arr = create_arr(elements_list)
    index = create_index(arr, block_size)
    
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, f"Índices: {index}\n")
    text_result.insert(tk.END, f"Tamaño del arreglo: {len(arr)}\n\n")
    
    result = indexed_sequential_search(arr, index, target, ascending)
    text_result.insert(tk.END, result)


def open_main_window():
    splash_screen.destroy()
    
    global root
    root = tk.Tk()
    root.title("Indexed Sequential Search")
    root.attributes('-fullscreen', True)

    tk.Label(root, text="Ingrese los elementos del arreglo separados por comas:", font=("Helvetica", 18)).pack(pady=20)
    global entry_elements
    entry_elements = tk.Entry(root, width=60, font=("Helvetica", 18))
    entry_elements.pack(pady=20)

    tk.Label(root, text="\nIngrese el tamaño del bloque:", font=("Helvetica", 18)).pack(pady=20)
    global entry_block_size
    entry_block_size = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_block_size.pack(pady=20)

    tk.Label(root, text="\nIngrese el elemento a buscar:", font=("Helvetica", 18)).pack(pady=20)
    global entry_target
    entry_target = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_target.pack(pady=20)

    btn_search_asc = tk.Button(root, text="Buscar a la derecha", font=("Helvetica", 18), command=lambda: search(True))
    btn_search_asc.pack(pady=20)

    btn_search_desc = tk.Button(root, text="Buscar a la izquierda", font=("Helvetica", 18), command=lambda: search(False))
    btn_search_desc.pack(pady=20)

    global text_result
    text_result = tk.Text(root, height=100, width=100, font=("Helvetica", 18))
    text_result.pack(pady=5)

    root.mainloop()

def open_pdf():
    pdf_path = "Secuencial_Indexada.pdf"  # Ruta del archivo PDF existente
    os.system(f"open {pdf_path}")

splash_screen = tk.Tk()
splash_screen.title("Bienvenido")

tk.Label(splash_screen, text="Método de Búsqueda Secuencial Indexada", font=("Helvetica", 30)).pack(pady=20)
tk.Label(splash_screen, text="La búsqueda secuencial indexada es una técnica que combina la búsqueda secuencial tradicional con un índice previo para optimizar el proceso de búsqueda, especialmente en listas grandes. ", wraplength=800, font=("Helvetica", 20)).pack(pady=20)

btn_pdf = tk.Button(splash_screen, text="Conozca más sobre el método de búsqueda secuencial indexada", font=("Helvetica", 20), command=open_pdf)
btn_pdf.pack(pady=20)

tk.Label(splash_screen, text="Integrantes del equipo:", font=("Helvetica", 25)).pack(pady=20)
tk.Label(splash_screen, text="1. Negron, Danna\n2. Patiño, Hugo\n3. Rios, Sebastian", font=("Helvetica", 20)).pack(pady=20)

btn_proceed = tk.Button(splash_screen, text="Continuar", font=("Helvetica", 20), command=open_main_window)
btn_proceed.pack(pady=20)

splash_screen.mainloop()