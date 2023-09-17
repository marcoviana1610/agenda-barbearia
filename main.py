import tkinter as tk
from tkinter import ttk

# Dicionário para armazenar os horários agendados
agenda = {
    "09:00 AM": None,
    "10:00 AM": None,
    "11:00 AM": None,
    "12:00 PM": None,
    "01:00 PM": None,
    "02:00 PM": None,
    "03:00 PM": None,
    "04:00 PM": None,
    "05:00 PM": None,
}

def agendar_horario():
    nome_cliente = nome_entry.get()
    horario_selecionado = horario_combobox.get()
    
    if nome_cliente.strip() == "":
        resultado_label.config(text="Por favor, insira o nome do cliente.", foreground="red")
        return
    
    if agenda[horario_selecionado] is not None:
        resultado_label.config(text=f"O horário {horario_selecionado} já está agendado para {agenda[horario_selecionado]}.", foreground="red")
    else:
        agenda[horario_selecionado] = nome_cliente
        resultado_label.config(text=f"Agendamento para {nome_cliente} às {horario_selecionado}.", foreground="green")
        horario_combobox.set("Escolha um horário")
        listar_agendamentos()

def listar_agendamentos():
    lista_agendamentos.delete(0, tk.END)
    for horario, cliente in agenda.items():
        lista_agendamentos.insert(tk.END, f"{horario}: {cliente}")

# Configuração da janela principal
root = tk.Tk()
root.title("Agendamento de Barbearia")

# Estilo visual personalizado com tema dark
style = ttk.Style()
style.configure('TButton', background='blue', foreground='white', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12), foreground='white', background='#333')
style.configure('TFrame', background='#333')
style.map('TButton', background=[('active', '#555')])

# Frame principal
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Rótulo e entrada para o nome do cliente
nome_label = ttk.Label(main_frame, text="Nome do Cliente:")
nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nome_entry = ttk.Entry(main_frame, font=('Helvetica', 12), foreground='black')
nome_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Rótulo e caixa de combinação para escolher o horário
horario_label = ttk.Label(main_frame, text="Escolha um horário:")
horario_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
horario_combobox = ttk.Combobox(main_frame, values=list(agenda.keys()), font=('Helvetica', 12))
horario_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Botão para agendar o horário
agendar_button = ttk.Button(main_frame, text="Agendar", command=agendar_horario)
agendar_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

# Rótulo para exibir o resultado
resultado_label = ttk.Label(main_frame, text="", font=('Helvetica', 12))
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Lista para exibir os agendamentos
lista_agendamentos = tk.Listbox(main_frame, width=50, height=10, font=('Helvetica', 12), background='#333', foreground='white')
lista_agendamentos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Configuração do layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Configuração do tema dark
root.tk_setPalette(background='#333')

# Iniciar a interface gráfica
root.mainloop()