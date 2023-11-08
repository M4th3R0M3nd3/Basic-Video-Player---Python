import sqlite3
from tkinter import *
from tkinter import ttk

def cadastrar_usuario():
    usuario_inserido = entry_novo_usuario.get()
    senha_inserida = entry_nova_senha.get()

    # Conecta-se ao banco de dados SQLite (ou cria o arquivo se ele não existir)
    conn = sqlite3.connect("login_db.db")
    cursor = conn.cursor()

    # Insere o novo usuário e senha na tabela de usuários
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario_inserido, senha_inserida))
    conn.commit()
    conn.close()

    resultado_label.config(text="Cadastro realizado com sucesso!")

janela = Tk()
janela.title('Cadastro de Usuário')

frm = ttk.Frame(janela, padding=10)
frm.grid()

ttk.Label(frm, text="Cadastro de Usuário").grid(column=0, row=0, columnspan=2)
ttk.Label(frm, text="Novo Usuário:").grid(column=0, row=1)
ttk.Label(frm, text="Nova Senha:").grid(column=0, row=2)

entry_novo_usuario = ttk.Entry(frm)
entry_novo_usuario.grid(column=1, row=1)
entry_nova_senha = ttk.Entry(frm, show="*")
entry_nova_senha.grid(column=1, row=2)

cadastrar_button = ttk.Button(frm, text="Cadastrar", command=cadastrar_usuario)
cadastrar_button.grid(column=1, row=3)

resultado_label = ttk.Label(frm, text="")
resultado_label.grid(column=0, row=4, columnspan=2)

janela.mainloop()
