"""
ALBUM MUNDIAL 2026 — Launcher
Doble click para abrir. No muestra consola (extension .pyw).
"""
import subprocess, webbrowser, time, os, sys
try:
    from urllib.request import urlopen
except ImportError:
    pass

BASE = os.path.dirname(os.path.abspath(__file__))
UVICORN = os.path.join(BASE, "venv", "Scripts", "uvicorn.exe")
PYTHON  = os.path.join(BASE, "venv", "Scripts", "python.exe")
SEED    = os.path.join(BASE, "scripts", "seed_full.py")
URL     = "http://127.0.0.1:8000"

def server_ok():
    try:
        urlopen(URL + "/health", timeout=1)
        return True
    except:
        return False

def run():
    # Si ya está corriendo, solo abrimos el navegador
    if server_ok():
        webbrowser.open(URL)
        return

    # Correr seed si no existe la base de datos
    db_path = os.path.join(BASE, "album.db")
    if not os.path.exists(db_path):
        subprocess.run(
            [PYTHON, SEED],
            cwd=BASE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

    # Iniciar uvicorn sin ventana de consola
    subprocess.Popen(
        [UVICORN, "app.main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=BASE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    # Esperar hasta que responda (max 20 seg)
    for _ in range(20):
        time.sleep(1)
        if server_ok():
            break

    webbrowser.open(URL)

run()
