import requests

API_KEY = 'sk-424ae0dda1904f69a4f2e0bf7e793517'
API_URL ='https://api.deepseek.com/v1/chat/completionss'

RESPUESTAS_PREDEFINIDAS = {
    "hola": "¡Hola! ¿Cómo estás?",
    "¿cómo estás?": "Estoy bien, gracias por preguntar.",
    "como estas": "Estoy bien, gracias por preguntar.",
    "Tengo una duda": "Claro, aca estoy para cualquier cosa, dime."
    "Necesito ayuda": "Que quieres preguntar"
    "Chao": "¡Hasta luego!",
    "chao": "¡Hasta luego!",
    "salir": "¡Hasta luego!"
}


def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': modelo,
        'messages': [{'role': 'user', 'content': mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', 'Sin respuesta')
    except requests.exceptions.HTTPError as err:
        return f"Error en la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

def main():
    print(" ¡Bienvenido al Chatbot de Lucho, Pregunta lo que quieras que aca te responderemos! ")
    print(" Escribe 'ayuda' para ver comandos o 'salir' para terminar.\n")

    while True:
        mensaje_usuario = input("Tú: ").lower() 

        if mensaje_usuario in RESPUESTAS_PREDEFINIDAS:
            print(f"Chatbot: {RESPUESTAS_PREDEFINIDAS[mensaje_usuario]}")
            if mensaje_usuario == "salir" or mensaje_usuario == "adiós" or mensaje_usuario == "adios":
                break
        elif mensaje_usuario == 'ayuda':
            print(" Comandos disponibles:")
            print("  - 'hola' → Saludo")
            print("  - '¿cómo estás?' → Estado del chatbot")
            print("  - 'Tengo una duda'→ Disponible para resolver preguntas")
            print("  - 'Necesito ayuda' → Disponible para resoler preguntas")
            print("  - 'adiós' o 'salir' → Terminar el chatbot\n")
            continue
        else:
            respuesta = enviar_mensaje(mensaje_usuario)
            print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
