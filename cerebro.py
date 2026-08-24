# cerebro.py
# Responde consultas frecuentes del gimnasio.
# Devuelve (texto, tema). El tema le sirve al conector para decidir
# si además hay que avisarle a un humano.

MENU = '''Te puedo ayudar con:
1 - Horarios
2 - Precios y planes
3 - Ubicación

Escribe el número o pregúntame directamente.'''
 

def detectar_tema(mensaje):
    """Traduce lo que escribió el usuario a un tema conocido."""
    mensaje = mensaje.strip().lower()

    if mensaje in ("0", "menu", "hola", "ayuda"):
        return "menu"

    elif mensaje == "1" or "horario" in mensaje or "que dias se entrena" in mensaje:
        return "horarios"

    elif (mensaje == "2" or "precio" in mensaje or "plan" in mensaje
          or "cuesta" in mensaje or "cuánto vale" in mensaje):
        return "precios"

    elif (mensaje == "3" or "ubicacion" in mensaje or "direccion" in mensaje
          or "donde queda" in mensaje):
        return "ubicacion"

    else:
        return "desconocido"


def responder(mensaje):
    """Devuelve una tupla (texto, tema) para el mensaje recibido."""
    tema = detectar_tema(mensaje)

    if tema == "menu":
        texto = "¡Hola! Bienvenido al gimnasio.\n\n" + MENU

    elif tema == "horarios":
        texto = '''Atendemos de lunes a domingo:
Lunes a viernes: 08:00 a 22:00
Sábados: 09:00 a 16:00
Domingos: 10:00 a 14:00'''

    elif tema == "precios":
        texto = '''Los planes disponibles son:
1 mes:    $25.000
3 meses:  $50.000
6 meses:  $75.000
12 meses: $90.000

¡Sin costo de matrícula, acceso libre!'''

    elif tema == "ubicacion":
        texto = '''Estamos ubicados en:
Independencia 87 (ex Manios)
Villa Nonguén'''

    else:
        texto = ("No tengo esa información, pero le avisé al equipo "
                 "y te responderán apenas puedan.\n\n" + MENU)

    return texto, tema


# --- Modo terminal: esto no es parte del cerebro, es un conector ---
if __name__ == "__main__":
    print("Escribe 'salir' para terminar.\n")

    bienvenida, _ = responder("hola")
    print(bienvenida)

    while True:
        entrada = input("\nTú: ")
        if entrada.strip().lower() == "salir":
            break

        texto, tema = responder(entrada)
        print("Bot:", texto)

        if tema == "desconocido":
            print(f"\n[AVISO AL COACH] Consulta sin respuesta: {entrada}")