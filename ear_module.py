import speech_recognition as sr
import brain_module
import mouth_module

def listen_and_transcribe():
    rec = sr.Recognizer()
    mic = sr.Microphone()

    modo_ia = False

    with mic as source:
        print("Calibrando ruido de fondo...")
        rec.adjust_for_ambient_noise(source,duration=1) #Mantener duration por arriba de 0.5 para que no se escuche el ruido de fondo
        mouth_module.speak("Hola, soy JARVIS, tu asistente personal. Estoy aquí para ayudarte en lo que necesites.") #Aviso por voz que el programa esta listo para escuchar

        while True:
            try:
                audio_data=rec.listen(source)
                transcription = rec.recognize_google(audio_data, language="es_AR")
                print(f"Escuche: {transcription}")

                if not modo_ia:
                    #Modo SIN IA de Gemini
                    if "computadora" in transcription.lower():
                        #Si escucha computadora cambia al brain_module y se comunica con gemini a partir de ahora
                        modo_ia = True
                        mouth_module.speak("Estoy para ayudarte en lo que necesites.") #Aviso por voz que ahora esta listo para recibir ordenes y responder con gemini
                
                else:
                    #Modo CON IA de Gemini
                    if "gracias" in transcription.lower():
                        #Si escucha gracias vuelve a solo escuchar
                        modo_ia = False
                        mouth_module.speak("De nada, estoy para ayudarte en lo que necesites.") #Aviso por voz que ahora esta listo para solo escuchar
                        print(" "*40)

                    else:
                        #Si esta activo, le manda todo al brain_module
                        if transcription.strip() != "":
                            if "*" in transcription.lower():
                                respuesta = transcription.replace("*", "").strip()
                                mouth_module.speak(respuesta)
                            else:
                                respuesta = brain_module.process_and_respond(transcription)
                                mouth_module.speak(respuesta)


                '''
                if "computadora" in transcription.lower():
                        #En un futuro creo que esto llamaria a que se llame el programa principal
                        #print("Detectada palabra para iniciar a J.A.R.V.I.S")

                        #Gemini me dijo que agregue esto poruqe sino la IA me daba una explicacion de por que no es una computadora
                        comando = transcription.replace("computadora", "").strip()

                        if comando != "":
                             
                            #Esto creo que llamaria al otro modulo y le pasaria lo que yo le digo a la IA
                            respuesta = brain_module.process_and_respond(comando)
                            print(f"J.A.R.V.I.S: {respuesta}\n")
                            print(" "*40)
                        else:
                            print("J.A.R.V.I.S: Estoy para ayudarte en lo que necesites.")
                '''
            
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Error de conexion con el servicio de reconocimiento: {e}") #Recomendado por speech_recognition, ni idea
            except Exception as e:
                print(f"Error inesperado: {e}")

if __name__ == "__main__":
    listen_and_transcribe()

#Para inicializarlo:
##cd J.A.R.V.I.S
##python ear_module.py