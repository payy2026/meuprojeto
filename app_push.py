from winotify import Notification, audio
import subprocess
from datetime import datetime
import time

BRANCH = "main"
LINK = "https://login.microsoftonline.com/"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def notificar(titulo, mensagem):
    toast = Notification(
        app_id="Git Push PRO",
        title=titulo,
        msg=mensagem,
        duration="short"
    )

    # 🔗 botão
    toast.add_actions(label="Entrar", launch=LINK)

    # 🔗 clicar na notificação inteira
    toast.launch = LINK

    toast.set_audio(audio.Default, loop=False)
    toast.show()

def fazer_push():
    msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    run("git add .")
    status = run("git status --porcelain")

    if not status.stdout.strip():
        notificar("Git Push", "Nada para commitar.")
    else:
        run(f'git commit -m "{msg}"')
        run(f"git push origin {BRANCH}")
        notificar("Outlook", "Push realizado com sucesso!")

# 🔁 roda a cada 25 minutos
while True:
    fazer_push()
    time.sleep(15)