from winotify import Notification, audio
import subprocess
from datetime import datetime
import time

BRANCH = "main"
LINK = "https://github.com/payy2026/meuprojeto"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def notificar(titulo, mensagem, link):
    toast = Notification(
        app_id="Git Push PRO",
        title=titulo,
        msg=mensagem,
        duration="short"
    )

    toast.add_actions(label="Abrir", launch=link)
    toast.launch = link

    toast.set_audio(audio.Default, loop=False)
    toast.show()

def fazer_push():
    msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    run("git add .")
    status = run("git status --porcelain")

    if not status.stdout.strip():
        notificar("Git Push", "Nada para commitar.", LINK)
    else:
        run(f'git commit -m "{msg}"')
        run(f"git push origin {BRANCH}")
        notificar("Git Push", "Push realizado!", LINK)

# 🔁 LOOP A CADA 25 MINUTOS
while True:
    print("Executando push...")
    fazer_push()

    print("Aguardando 25 minutos...")
    time.sleep(1500)  # 1500 segundos = 25 minutos