memoria = {}

def main():
    print("Bienvenido al chatbot de memoria. Puedes enseñarme cosas y preguntarme sobre ellas.")
    entrada = input("User: ")
    palabras = entrada.lower().split()
    while entrada.lower() != "salir":
        if len(palabras) >= 2 and palabras[0] == "me" and palabras[1] == "llamo":
            nombre = palabras[2]
            memoria["nombre"] = nombre
            print(f"Chatbot: ¡Encantado de conocerte, {nombre}!")
        elif len(palabras) >= 2  and palabras[0] == "tengo" and palabras[2] == "años":
            edad = palabras[1]
            memoria["edad"] = edad
            print(f"Chatbot: ¡Genial! Ahora sé que tienes {edad} años.")
        elif len(palabras) >= 2 and palabras[0] == "mi" and palabras[1] == "color" and palabras[2] == "favorito" and palabras[3] == "es":
            color = palabras[4]
            memoria["color_favorito"] = color
            print(f"Chatbot: ¡Perfecto! Ahora sé que tu color favorito es {color}.") 
        elif len(palabras) >= 2 and palabras[0] == "mi" and palabras[1] == "comida" and palabras[2] == "favorita" and palabras[3] == "es":
            comida = palabras[4]
            memoria["comida_favorita"] = comida
            print(f"Chatbot: ¡Delicioso! Ahora sé que tu comida favorita es {comida}.")
        elif len(palabras) >= 2 and palabras[0] == "vivo" and palabras[1] == "en":
            ciudad = palabras[2]
            memoria["ciudad"] = ciudad
            print(f"Chatbot: ¡Qué interesante! Ahora sé que vives en {ciudad}.")  
        elif len(palabras) >= 2 and palabras[0] == "como" and palabras[1] == "me" and palabras[2] == "llamo":
            if "nombre" in memoria:
                print(f"Chatbot: Tu nombre es {memoria['nombre']}.")
            else:
                print("Chatbot: No sé tu nombre. Por favor, dime cómo te llamas.")
        elif len(palabras) >= 2 and palabras[0] == "cuantos" and palabras[1] == "años" and palabras[2] == "tengo":
            if "edad" in memoria:
                print(f"Chatbot: Tienes {memoria['edad']} años.")
            else:
                print("Chatbot: No sé tu edad. Por favor, dime cuántos años tienes.")
        elif len(palabras) >= 2 and palabras[0] == "cual" and palabras[1] == "es" and palabras[2] == "mi" and palabras[3] == "color":
            if "color_favorito" in memoria:
                print(f"Chatbot: Tu color favorito es {memoria['color_favorito']}.")
            else:
                print("Chatbot: No sé tu color favorito. Por favor, dime cuál es.")
        elif len(palabras) >= 2 and palabras[0] == "cual" and palabras[1] == "es" and palabras[2] == "mi" and palabras[3] == "comida":
            if "comida_favorita" in memoria:
                print(f"Chatbot: Tu comida favorita es {memoria['comida_favorita']}.")
            else:
                print("Chatbot: No sé tu comida favorita. Por favor, dime cuál es.")
        elif len(palabras) >= 2 and palabras[0] == "donde" and palabras[1] == "vivo":
            if "ciudad" in memoria:
                print(f"Chatbot: Vives en {memoria['ciudad']}.")
            else:
                print("Chatbot: No sé dónde vives. Por favor, dime dónde vives.")
            
        entrada = input("User: ")
        palabras = entrada.lower().split()

main()
