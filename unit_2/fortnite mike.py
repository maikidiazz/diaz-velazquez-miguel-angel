def show_menu():
    print("\n-Fortnite Obby-")
    print("Cual va ser la eleccion de hoy")
    print("1 Technology (Mapas creativo)")
    print("2 Action (Zonas para caer)")
    print("3 Science Fiction (Lore de fortnite y Modos Raros)")


def get_genre():
    opcion_elegida = input("Elige una opcion del 1 al 3, no otra menso: ")
    return opcion_elegida


def recommend_content(genre):
    catalogo_fortnite = {
        "1": [
            "activar el Modo Rendimiento (+200 FPS) para q no te quejes del lag y que no se caliente la lap",
            "configurar DPI del mouse a 800 y 12 de sensibilidad",
            "quejarte del lag y de los tryhards"
        ],
        "2": [
            "caer directo en Pisos Picados , la verdad esta mjr parque placentero",
            "rushear con escopeta ",
            "agarrar una llama y rushear"
        ],
        "3": [
            "Investigar los misterios del Cubo Kevin en el mapa",
            "Jugar el modos raros",
            "Ver el evento de fin de temporada"
        ]
    }
    return catalogo_fortnite.get(genre, [])


def rate_content():
    print("\n toca calificar")
    while True:
        try:
            estrellas = int(input(" Dale de 1 a 5 estrellas: "))
            if 1 <= estrellas <= 5:
                print(f"mm ok, guardamos tus {estrellas} eso, (no lo guardo)")
                break
            else:
                print("sea serio, pon un numero del 1 al 5.")
        except ValueError:
            print("Escribe un numero real, ya por favor y gracias")


def main():
    while True:
        show_menu()
        opcion = get_genre()
        
        ideas = recommend_content(opcion)
        
        if ideas:
            print("\nrecomendaciones no propias ")
            for idea in ideas:
                print(f"-> {idea}")
            
            rate_content()
        else:
            print("\nesa opcion ni existe en el juego, ponle bien")
        
        repetir = input("\nQuieres otra? (S/N): ").strip().lower()
        if repetir != 's':
            print("Saliendo del lobby por fnin")
            break


if __name__ == "__main__":
    main()