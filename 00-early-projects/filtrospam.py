spam = {"dinero": 2, "premio": 3, "gratis": 1, "oferta": 2, "urgente": 3, "click": 1, "ganar": 2, 
        "descuento": 1, "compra": 1, "ahora": 1, "promocion": 2, "regalo": 1, "increible": 2, "exclusivo": 3, 
        "limitado": 2, "urgente": 3,}

no_spam = {"hola": 1, "gracias": 1, "saludos": 1, "informacion": 1, "consulta": 1, "reunion": 2,
        "proyecto": 2, "actualizacion": 1, "notificacion": 1, "confirmacion": 1, "documento": 1, 
        "invitacion": 2, "agenda": 1, "recordatorio": 1, "respuesta": 1, "mensaje": 1, "correo": 1, 
        "asunto": 1, "noticia": 1, "evento": 2,}

def main():
    correo_recibido = input("Introduce el correo recibido: ").lower().split()
    palabras_spam = 0
    palabras_no_spam = 0

    for palabra in correo_recibido:
        palabra = palabra.strip(".,!?;:")
        if palabra in spam:
            palabras_spam += spam[palabra]
        elif palabra in no_spam:
            palabras_no_spam += no_spam[palabra]

    if palabras_spam >= 1 and palabras_spam > palabras_no_spam:
        print(f"El correo es spam")
    else:
        print(f"El correo no es spam")
main()