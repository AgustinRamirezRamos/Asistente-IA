from gtts import gTTS
import pygame
import os
import time

def hablar_con_google(texto):
    print("Generando audio con google")
    
    #1. Generamos el audio con gTTS
    #El .com.ar en tld hace que tenga un acento mas argentino, si se lo saco suena mas neutro
    tts = gTTS(text=texto, lang='es', tld='com.ar')

    #2. Guardamos el audio en un archivo temporal
    archivo_temporal = "temp_audio.mp3"
    tts.save(archivo_temporal)

    #3. Inicializamos el mezclador de audio y reproducimos
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_temporal)
    pygame.mixer.music.play()

    #4 Esperamos a que termine de hablar antes de seguir
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    #5. Apagamos el reproductor y borramos el achivo para dejar todo limpio
    pygame.mixer.quit()

    #Pausa agregada por gemini para que supuestamente Windows suelte el archivo antes de borrarlo
    time.sleep(0.1)
    os.remove(archivo_temporal)

if __name__ == "__main__":
    hablar_con_google("Hola, soy JARVIS, tu asistente personal. Estoy aquí para ayudarte en lo que necesites.")