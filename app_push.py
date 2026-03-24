import subprocess
from datetime import datetime
import tkinter as tk
import threading
import winsound

BRANCH = "main"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 🔔 Notificação estilo iPhone
def mostrar_notificacao(texto):
    notif = tk.Toplevel()
    notif.overrideredirect(True)
    notif.configure(bg="#111")

    largura = 300
    altura = 80

    x = notif.winfo_screenwidth() - largura - 10
    y = -100  # começa fora da tela

    notif.geometry(f"{largura}x{altura}+{x}+{y}")

    label = tk.Label(
        notif,
        text=texto,
        fg="white",
        bg="#111",
        font=("Arial", 10),
        wraplength=280,
        justify="left"
    )
    label.pack(padx=10, pady=10)

    # 🔊 som
    try:
        winsound.Beep(1000, 200)
    except:
        pass

    # animação descendo
    def descer():
        nonlocal y
        if y < 50:
            y += 5
            notif.geometry(f"{largura}x{altura}+{x}+{y}")
            notif.after(10, descer)
        else:
            notif.after(3000, subir)

    # animação subindo
    def subir():
        nonlocal y
        if y > -100:
            y -= 5
            notif.geometry(f"{largura}x{altura}+{x}+{y}")
            notif.after(10, subir)
        else:
            notif.destroy()

    descer()

# 🚀 Função de push
def fazer_push():
    msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    run("git add .")
    status = run("git status --porcelain")

    if not status.stdout.strip():
        mostrar_notificacao("⚠️ Nada para commitar.")
    else:
        run(f'git commit -m "{msg}"')
        run(f"git push origin {BRANCH}")
        mostrar_notificacao("✅ Push realizado com sucesso!")

# 🖥️ Interface principal
janela = tk.Tk()
janela.title("Git Push PRO")
janela.geometry("300x150")
janela.configure(bg="#222")

titulo = tk.Label(janela, text="Git Push PRO", fg="white", bg="#222", font=("Arial", 16))
titulo.pack(pady=10)

botao = tk.Button(
    janela,
    text="Fazer Push",
    command=lambda: threading.Thread(target=fazer_push).start(),
    height=2,
    width=20,
    bg="#007AFF",
    fg="white",
    bd=0
)
botao.pack(pady=20)

janela.mainloop()