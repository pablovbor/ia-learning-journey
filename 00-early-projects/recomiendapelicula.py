peliculas = {
    "Matrix": {"generos": ["ficcion", "accion"], "duracion": 136},
    "Titanic": {"generos": ["romance", "drama"], "duracion": 194},
    "Rocky": {"generos": ["deporte", "drama"], "duracion": 119},
    "Interstellar": {"generos": ["ficcion", "aventura"], "duracion": 169},
    "Star wars": {"generos": ["ficcion", "aventura"], "duracion": 121},
    "El padrino": {"generos": ["drama", "crimen"], "duracion": 175},
    "Forrest Gump": {"generos": ["drama", "comedia"], "duracion": 142},
    "La lista de Schindler": {"generos": ["drama", "historia"], "duracion": 195},
    "Pulp Fiction": {"generos": ["crimen", "drama"], "duracion": 154},
    "Cadena perpetua": {"generos": ["drama", "crimen"], "duracion": 129},
    "Origen": {"generos": ["ficcion", "accion"], "duracion": 148},
    "Gladiador": {"generos": ["accion", "drama"], "duracion": 155},
    "El señor de los anillos": {"generos": ["ficcion", "aventura", "accion"], "duracion": 201},
}

def main():
    print("Bienvenido al recomendador de peliculas.")
    gustos = input("Por favor, ingrese un genero de pelicula (ficcion, accion, romance," \
    " drama, deporte, aventura, crimen, comedia, historia): ").lower().split()
    tiempo = int(input("Ingrese el tiempo disponible para ver la pelicula (en minutos): "))
    mejor_pelicula = None
    max_puntos = 0
    for pelicula, caracteristicas in peliculas.items():
        puntos = 0
        if caracteristicas["duracion"] <= tiempo:
            for genero in caracteristicas["generos"]:
                if genero in gustos:
                    puntos += 1
                    if puntos > max_puntos:
                        max_puntos = puntos
                        mejor_pelicula = pelicula
        if puntos >= 1:
            print(f"Pelicula que podria interesarle: {pelicula}")
    print(f"\nPelicula mas recomendada para usted: {mejor_pelicula}")
main()