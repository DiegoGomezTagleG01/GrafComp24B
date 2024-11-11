# main.py
from pollo import ShowChicken
from escena import DaytimeScene

if __name__ == "__main__":
    # Crear la primera escena y renderizarla
    scene = ShowChicken()
    scene.render()

    # Crear la segunda escena y renderizarla
    scene = DaytimeScene()
    scene.render()
