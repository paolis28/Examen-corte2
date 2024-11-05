import tkinter as tk
from tkinter import messagebox
import re
from unidecode import unidecode

def es_palindromo(texto):
    texto = unidecode(texto).lower()
    texto = re.sub(r'[^a-zA-Z0-9]', '', texto)
    return texto == texto[::-1]

def validar_palindromo():
    texto = entry_texto.get()
    if es_palindromo(texto):
        messagebox.showinfo("Resultado", "Es un palíndromo.")
    else:
        messagebox.showinfo("Resultado", "No es un palíndromo.")

def limpiar_texto():
    entry_texto.delete(0, tk.END)  

root = tk.Tk()
root.title("Verificador de Palíndromos")
root.configure(bg='#333333') 

label = tk.Label(root, text="Ingrese un texto:", bg='#333333', fg='#FFFFFF', font=('Arial', 14))
label.pack(pady=10)
entry_texto = tk.Entry(root, width=80, font=('Arial', 14), bg='#666666', fg='#FFFFFF', insertbackground='white')
entry_texto.pack(pady=10)

boton_validar = tk.Button(root, text="Validar", command=validar_palindromo, bg='#555555', fg='#FFFFFF', font=('Arial', 12))
boton_validar.pack(pady=10)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_texto, bg='#555555', fg='#FFFFFF', font=('Arial', 12))
boton_limpiar.pack(pady=10)


root.mainloop()
