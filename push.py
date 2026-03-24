import subprocess
from datetime import datetime
from plyer import notification

BRANCH = "main"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

msg = f"Auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

print("Adicionando arquivos...")
run("git add .")

status = run("git status --porcelain")

if not status.stdout.strip():
    print("Nada para commitar.")

    notification.notify(
        title="Git Push",
        message="Nada para commitar.",
        timeout=5
    )
else:
    print("Fazendo commit...")
    run(f'git commit -m "{msg}"')

    print("Enviando...")
    run(f"git push origin {BRANCH}")

    print("Push realizado com sucesso!")

    notification.notify(
        title="Git Push",
        message="Push realizado com sucesso!",
        timeout=5
    )