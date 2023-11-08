from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3
from frame import criar_janela_logado

def abrir_cadastro():
    subprocess.Popen(["python", "cadastro.py"])

def verificar_login(janela_login):
    usuario_inserido = entry_usuario.get()
    senha_inserida = entry_senha.get()

    conn = sqlite3.connect("login_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario_inserido, senha_inserida))
    resultado = cursor.fetchone()

    if resultado:
        resultado_label.config(text="Login bem-sucedido!!")
        # Após o login bem-sucedido, chame a função para criar a área logada
        criar_janela_logado()

        # Feche a janela de login
        janela_login.destroy()
    else:
        resultado_label.config(text="Login falhou. Verifique seu usuário e senha.")

    conn.close()

if __name__ == '__main__':
    janela = Tk()
    janela.title('Sistema de Login')

    frm = ttk.Frame(janela, padding=10)
    frm.grid()

    ttk.Label(frm, text="Login").grid(column=0, row=0, columnspan=2)
    ttk.Label(frm, text="Usuário:").grid(column=0, row=1)
    ttk.Label(frm, text="Senha:").grid(column=0, row=2)

    cadastro_button = ttk.Button(frm, text="Cadastrar Usuário", command=abrir_cadastro)
    cadastro_button.grid(column=1, row=5)
    entry_usuario = ttk.Entry(frm)
    entry_usuario.grid(column=1, row=1)
    entry_senha = ttk.Entry(frm, show="*")
    entry_senha.grid(column=1, row=2)

    login_button = ttk.Button(frm, text="Login", command=lambda: verificar_login(janela))
    login_button.grid(column=1, row=3)

    resultado_label = ttk.Label(frm, text="")
    resultado_label.grid(column=0, row=4, columnspan=2)

    janela.mainloop()
