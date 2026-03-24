import subprocess
from datetime import datetime
import tkinter as tk
import threading

BRANCH = "main"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 🔥 Popup moderno
def popup(msg):
    notif = tk.Toplevel()
    notif.overrideredirect(True)  # remove borda
    notif.attributes("-topmost", True)
    notif.configure(bg="#1e1e1e")

    largura = 320
    altura = 90

    x = notif.winfo_screenwidth() - largura - 10
    y = -100

    notif.geometry(f"{largura}x{altura}+{x}+{y}")

    frame = tk.Frame(notif, bg="#1e1e1e")
    frame.pack(fill="both", expand=True)

    titulo = tk.Label(frame, text="Git Push", fg="#00ffcc", bg="#1e1e1e", font=("Arial", 12, "bold"))
    titulo.pack(anchor="w", padx=10, pady=(8,0))

    texto = tk.Label(frame, text=msg, fg="white", bg="#1e1e1e", font=("Arial", 10), wraplength=300, justify="left")
    texto.pack(anchor="w", padx=10)

    # animação descendo
    def descer():
        nonlocal y
        if y < 40:
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

# 🚀 Push
def fazer_push():
    msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    run("git add .")
    status = run("git status --porcelain")

    if not status.stdout.strip():
        popup("⚠️ Nada para commitar.")
    else:
        run(f'git commit -m "{msg}"')
        run(f"git push origin {BRANCH}")
        popup("✅ Push realizado com sucesso!")

# 🖥️ Interface
janela = tk.Tk()
janela.title("Git Push PRO")
janela.geometry("300x150")
janela.configure(bg="#111")

titulo = tk.Label(janela, text="Git Push PRO", fg="white", bg="#111", font=("Arial", 16))
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