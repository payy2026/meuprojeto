from winotify import Notification, audio
import subprocess
from datetime import datetime

BRANCH = "main"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def notificar(titulo, mensagem):
    toast = Notification(
        app_id="OUTLOOK.COM",
        title=titulo,
        msg=mensagem,
        icon=""  # opcional: caminho de ícone .ico
    )

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
        notificar("Git Push", "Microsoft-365/outlook.  Conta Bloqueada.")

fazer_push()