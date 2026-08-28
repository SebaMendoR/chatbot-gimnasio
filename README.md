# Chatbot Gimnasio

Chatbot que responde consultas frecuentes de un gimnasio real (AlfaStrong).

## Por qué existe

El coach responde las mismas preguntas todos los días por mensaje directo:
horarios, precios y métodos de pago. Este bot las contesta automáticamente
y avisa cuando aparece algo que necesita a una persona.

## Cómo funciona

El proyecto está separado en dos partes:

- **`cerebro.py`**: recibe un texto y devuelve `(respuesta, tema)`.
  No sabe por qué plataforma llegó el mensaje.
- **Conectores**: traducen entre una plataforma y el cerebro.
  Hoy existen dos, el modo terminal y `bot_telegram.py`.

Agregar una plataforma nueva significa escribir un conector, no tocar la lógica.

La detección funciona en tres capas: menú numerado, palabras clave y,
si todo lo anterior falla, comparación por parecido para tolerar errores
de tipeo (`difflib`). Los mensajes se normalizan antes de compararlos,
así que las tildes y las mayúsculas no afectan.

Cuando el tema queda en `desconocido` o el usuario pide hablar con una
persona, el conector deja un aviso para el coach.

## Cómo correrlo

Modo terminal, sin dependencias externas:

```
python cerebro.py
```

Modo Telegram (necesita un archivo `.env` con `TELEGRAM_TOKEN`):

```
pip install -r requirements.txt
python bot_telegram.py
```

## Estado

v2: funcionando en Telegram con contenido real del gimnasio.
Siguiente paso: conector de Instagram vía Meta for Developers.

## Limitaciones conocidas

- Las palabras clave genéricas capturan mensajes de otro tema.
  Ejemplo: "se puede congelar el plan" responde precios, porque
  el mensaje contiene la palabra "plan".
- Si un mensaje menciona dos temas, solo responde el primero.
- El aviso al coach sale por la terminal del PC donde corre el bot;
  todavía no le llega a él directamente.
- Los precios y horarios están escritos dentro del código. Cambiarlos
  requiere editar `cerebro.py`.