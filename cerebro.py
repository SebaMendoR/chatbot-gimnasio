# cerebro.py
# Responde consultas frecuentes del gimnasio.
# Devuelve (texto, tema). El tema le sirve al conector para decidir
# si además hay que avisarle a un humano.
import unicodedata

MENU = '''Te puedo ayudar con:
1 - Horarios
2 - Precios y planes
3 - Ubicación
4 - Métodos de pago

Escribe el número o pregúntame directamente.'''
 
def normalizar(texto):
    """Pasa a minúsculas, quita espacios sobrantes y elimina tildes."""
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def detectar_tema(mensaje):
    """Traduce lo que escribió el usuario a un tema conocido."""
    mensaje = normalizar(mensaje)
    
    if mensaje in ("0", "menu", "hola", "ayuda"):
        return "menu"

    elif mensaje == "1" or "horario" in mensaje or "que dias se entrena" in mensaje:
        return "horarios"

    elif (mensaje == "2" or "precio" in mensaje or "plan" in mensaje
          or "cuesta" in mensaje or "cuanto vale" in mensaje):
        return "precios"

    elif (mensaje == "3" or "ubicacion" in mensaje or "direccion" in mensaje
          or "donde queda" in mensaje):
        return "ubicacion"

    elif (mensaje == "4" or "pago" in mensaje or "pagar" in mensaje
          or "efectivo" in mensaje or "tarjeta" in mensaje
          or "transferencia" in mensaje or "debito" in mensaje
          or "credito" in mensaje):
        return "pagos"

    else:
        return "desconocido"


def responder(mensaje):
    """Devuelve una tupla (texto, tema) para el mensaje recibido."""
    tema = detectar_tema(mensaje)

    if tema == "menu":
        texto = "¡Hola! Somos AlfaStrong, Soy tu Asistente Virtual.\n\n" + MENU

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

    elif tema == "pagos":
        texto = '''Puedes pagar con:
- Efectivo
- Tarjeta de débito
- Tarjeta de crédito
- Transferencia'''

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