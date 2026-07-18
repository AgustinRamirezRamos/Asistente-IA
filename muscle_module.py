import subprocess
import webbrowser
import os

def open_vscode():
    print("Abriendo Visual Studio Code...")
    try:
        subprocess.Popen(["cmd", "/c", "code"], shell=True)
        return "Visual Studio Code se ha abierto correctamente."
    except Exception as e:
        return f"Hubo un error al abrir Visual Studio Code: {e}"
    
def search_web(busqueda):
    print(f"Buscando en la web: {busqueda}")
    url = f"https://www.google.com/search?q={busqueda}"
    webbrowser.open(url)
    return f"Buscando '{busqueda}' en internet."

def open_youtube(video):
    print(f"buscando en YouTube {video}")
    url = f"https://www.youtube.com/results?search_query={video}"
    webbrowser.open(url)
    return f"Abriendo YouTube para '{video}'."

if __name__ == "__main__":
    # open_vscode()
    # search_web("documentación de python")
    open_youtube("música para programar")