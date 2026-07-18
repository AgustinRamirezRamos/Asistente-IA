from gtts import gTTS
import pygame
import os
import time
import edge_tts
import asyncio

async def generar_audio(text, archivo_salida):
    com = edge_tts.Communicate(text, "es-AR-TomasNeural")
    await com.save(archivo_salida)

def speak(texto):
    print(f"JARVIS:{texto}")
    archivo_temporal = "temp_audio.mp3"

    try:
        
        asyncio.run(generar_audio(texto, archivo_temporal))
        

        pygame.mixer.init()
        pygame.mixer.music.load(archivo_temporal)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        time.sleep(0.1)
        if os.path.exists(archivo_temporal):
            os.remove(archivo_temporal)
        
    except Exception as e:
        print(f"Error en mouth_module: {e}")

if __name__ == "__main__":
    speak("Hola, soy JARVIS, tu asistente personal. Estoy aquí para ayudarte en lo que necesites.")