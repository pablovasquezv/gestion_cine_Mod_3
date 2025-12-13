"""Datos de películas y salas del cine.

    Tipo: dict anidado (dict → dict)

    Propósito: Sistema reservas cine

    Claves principales: Nombres películas (6 total)

    Datos: Horarios con boletos + precio fijo

"""

PELICULAS = {
    "Avengers Endgame": {
        "horarios": {"16:30": 100,"20:30": 100, "22:30": 80}, 
        "precio": 8500
    },
    "Spider-Man 2": {
        "horarios": {"16:40": 75, "20:00": 100}, 
        "precio": 7500
    },
    "Batman": {
        "horarios": {"14:10": 60,"19:10": 60,"22:10": 60}, 
        "precio": 9500
    },
    "Los ilusionistas 3": {
        "horarios": {"19:00": 70, "21:50": 50}, 
        "precio": 7000
    },
    "Jujutsu kaisen ejecución": {
        "horarios": {"22:20": 85}, 
        "precio": 8000
    },
    "Depredador: tierras salvajes": {
        "horarios": {"19:50": 63, "21:50": 69}, 
        "precio": 9000
    }
}
