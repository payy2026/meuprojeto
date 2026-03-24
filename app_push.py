import subprocess
from datetime import datetime
import webbrowser
import os

BRANCH = "main"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def abrir_notificacao(msg):
    caminho = os.path.abspath("notificacao.html")
    webbrowser.open(f"file://{caminho}")

def fazer_push():
    msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    run("git add .")
    status = run("git status --porcelain")

    if not status.stdout.strip():
        abrir_notificacao("Nada para commitar")
    else:
        run(f'git commit -m "{msg}"')
        run(f"git push origin {BRANCH}")
        abrir_notificacao("Push realizado com sucesso!")

fazer_push()