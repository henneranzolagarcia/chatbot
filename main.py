from fastapi import FastAPI
from google import genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite todos los orígenes
    allow_credentials=False,   # ¡Ojo! Debe ser False si usas "*"
    allow_methods=["*"],      # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],      # Permite todos los encabezados
)


client = genai.Client()

historial_de_mensajes = []

@app.get("/chat/{saludo}")
def llamar_ia(saludo):
    global historial_de_mensajes
    texto_historial = "/".join(historial_de_mensajes) 
    print("historial_de_mensajes: ", historial_de_mensajes)
    print("prompt al LLM: ", saludo + " --- Historial de mensajes: " + texto_historial)
    inferencia = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=saludo + " --- Historial de mensajes: " + texto_historial
    )
    historial_de_mensajes.append(saludo)
    return {"Respuesta": inferencia.output_text }
