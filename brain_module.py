import google.generativeai as glai
import muscle_module

API_KEY = "AIzaSyA9Q-j75QRH9_wD8TxEB4pC-uwfnlczMY0"
glai.configure(api_key=API_KEY)

#Puse Flash porque por ahora solo va a ser un agente de voz, mas adelante vere
model = glai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[
        muscle_module.open_vscode,
        muscle_module.search_web,
        muscle_module.open_youtube
    ])

#Inicio una conversacion vacia para que tenga memoria
chat = model.start_chat(enable_automatic_function_calling=True)

def process_and_respond(texto):

    #Con esta funcion se toma "texto", se lo manda a gemini y devuelve la respuesta

    try:
        print("Procesando")
        resp = chat.send_message(texto)
        return resp.text

        #Por si deja de andar gemini-2.5-flash correr este for dado por gemini
        #for m in genai.list_models():
            # Filtramos solo los modelos que sirven para generar texto/chat
            #if 'generateContent' in m.supported_generation_methods:
                #print("-", m.name)

    except Exception as e:
        return f"Hubo un error en brain_module: {e}"
    
if __name__ == "__main__":
    process_and_respond()