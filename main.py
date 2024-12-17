'''import tkinter as tk
from controllers import *

janela = tk.Tk()
janela.title("CRUD")
janela.geometry("300x400")

entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=10)

btn_adicionar_entrada = tk.Button(janela, text="Adicionar Entrada", command=adicionar_entrada)
btn_adicionar_entrada.pack(pady=5)

btn_adicionar_saida = tk.Button(janela, text="Adicionar Saida", command=adicionar_saida)
btn_adicionar_saida.pack(pady=5)

btn_remover = tk.Button(janela, text="Remover", command=remover_financa)
btn_remover.pack(pady=5)

lista = tk.Listbox(janela, font=("Arial", 12), height=10)
lista.pack(pady=10)

janela.mainloop()'''

import tkinter as tk
from tkinter import ttk

# Função para mostrar o layout de inserção de dados da função A
def mostrar_funcao_a():
    esconder_frames()
    frame_funcao_a.pack(fill="both", expand=True)

# Função para mostrar o layout de inserção de dados da função B
def mostrar_funcao_b():
    esconder_frames()
    frame_funcao_b.pack(fill="both", expand=True)

# Função para retornar ao menu inicial
def voltar_menu():
    esconder_frames()
    frame_menu.pack(fill="both", expand=True)

# Função para esconder todos os frames
def esconder_frames():
    frame_menu.pack_forget()
    frame_funcao_a.pack_forget()
    frame_funcao_b.pack_forget()

# Janela principal
root = tk.Tk()
root.title("Interface com Troca de Layout")
root.geometry("400x300")

# ----- Frame Principal (Menu com Botões) -----
frame_menu = ttk.Frame(root)
frame_menu.pack(fill="both", expand=True)

label_menu = ttk.Label(frame_menu, text="Menu Principal", font=("Helvetica", 16))
label_menu.pack(pady=10)

botao_funcao_a = ttk.Button(frame_menu, text="Função A", command=mostrar_funcao_a)
botao_funcao_a.pack(pady=5)

botao_funcao_b = ttk.Button(frame_menu, text="Função B", command=mostrar_funcao_b)
botao_funcao_b.pack(pady=5)

# ----- Frame da Função A -----
frame_funcao_a = ttk.Frame(root)

label_funcao_a = ttk.Label(frame_funcao_a, text="Preencha os dados para Função A", font=("Helvetica", 14))
label_funcao_a.pack(pady=10)

entry_a1 = ttk.Entry(frame_funcao_a)
entry_a1.pack(pady=5)
entry_a1.insert(0, "Campo 1")

entry_a2 = ttk.Entry(frame_funcao_a)
entry_a2.pack(pady=5)
entry_a2.insert(0, "Campo 2")

botao_voltar_a = ttk.Button(frame_funcao_a, text="Voltar", command=voltar_menu)
botao_voltar_a.pack(pady=10)

# ----- Frame da Função B -----
frame_funcao_b = ttk.Frame(root)

label_funcao_b = ttk.Label(frame_funcao_b, text="Preencha os dados para Função B", font=("Helvetica", 14))
label_funcao_b.pack(pady=10)

entry_b1 = ttk.Entry(frame_funcao_b)
entry_b1.pack(pady=5)
entry_b1.insert(0, "Campo X")

entry_b2 = ttk.Entry(frame_funcao_b)
entry_b2.pack(pady=5)
entry_b2.insert(0, "Campo Y")

botao_voltar_b = ttk.Button(frame_funcao_b, text="Voltar", command=voltar_menu)
botao_voltar_b.pack(pady=10)

# Inicia com o frame do menu principal
root.mainloop()
