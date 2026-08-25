# Chatbot Gimnasio

Chatbot que responde consultas frecuentes de un gimnasio.

## Por qué existe

El coach responde las mismas preguntas todos los días por mensaje:
horarios, precios y ubicación. Este bot las contesta automáticamente.

## Cómo funciona

Menú numerado y palabras clave. Cuando no reconoce la consulta,
responde que un humano se va a contactar y deja registrado el aviso.

## Cómo correrlo

```
python cerebro.py
```


## Estado

v1 en terminal. Siguiente paso: conector de Telegram.

## Limitaciones conocidas

- No reconoce palabras con tilde ("cuánto" no calza con "cuanto")
- No tolera errores de tipeo ("orario", "precioo")
- Si un mensaje menciona dos temas, solo responde el primero