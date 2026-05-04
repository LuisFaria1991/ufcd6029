import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk  # precisa de instalar: pip install pillow

# Criar janela
root = tk.Tk()
root.title("Portfólio Pessoal")
root.geometry("500x650")
root.configure(bg="#f0f0f0")

# Frame principal
frame = Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=20)

# ===== FOTO =====
try:
    img = Image.open("./sessao_04_05_2026/Luis.jpg")  # coloca a tua foto na mesma pasta
    img = img.resize((120, 120))
    foto = ImageTk.PhotoImage(img)
    label_foto = Label(frame, image=foto, bg="white")
    label_foto.pack(pady=10)
except:
    Label(frame, text="(Sem foto)", bg="white").pack()

# ===== DADOS =====
Label(frame, text="Nome: Luís Faria", bg="white", font=("Arial", 16)).pack(anchor="w")
Label(frame, text="Idade: 35", bg="white", font=("Arial", 12)).pack(anchor="w")
Label(frame, text="Profissão: Operador de departamento de amostras", bg="white", font=("Arial", 12)).pack(anchor="w")
Label(frame, text="Estudante de: Técnico de Instalações Eletricas", bg="white", font=("Arial", 12)).pack(anchor="w")

# ===== EMAIL =====
Label(frame, text="Email: luisfaria_10@hotmail.com", bg="white", font=("Arial", 12)).pack(anchor="w", pady=10)

# ===== UFCDs =====
Label(frame, text="UFCD's Dadas:", bg="white", font=("Arial", 12, "bold")).pack(anchor="w")

ufcds = [
    "UFCD 6029 - Tecnologia e montagem de circuitos eletronicos",
    "UFCD 6051 - Programação",
   

]

for ufcd in ufcds:
    Label(frame, text="• " + ufcd, bg="white", font=("Arial", 11)).pack(anchor="w")

# ===== INICIAR =====
root.mainloop()