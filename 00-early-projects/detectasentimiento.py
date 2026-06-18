positivas = ["feliz", "bien", "genial", "excelente", "maravilloso", "fantástico", 
             "increíble", "positivo", "agradable", "satisfactorio"]
negativas = ["triste", "mal", "horrible", "terrible", "desagradable", "deprimente",
             "negativo", "insatisfactorio", "desastroso", "pésimo"]

def main():
    frase = input("Ingrese una frase: ")
    palabras = frase.lower().split()
    contador_positivas = 0
    contador_negativas = 0
    
    for palabra in palabras:
        palabra = palabra.strip(".,!?;:")
        if palabra in positivas:
            contador_positivas += 1
        elif palabra in negativas:
            contador_negativas += 1
    
    print(f"Cantidad de palabras positivas: {contador_positivas}")
    print(f"Cantidad de palabras negativas: {contador_negativas}")
main()