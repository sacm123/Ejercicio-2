import csv
import random
import time

class Pokemon:
    def __init__(self, pokedex_number, name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed):
        self.pokedex_number = pokedex_number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

    def __str__(self):
        return f"{self.name} ({self.type_1}/{self.type_2}) - HP: {self.hp}, Atk: {self.attack}, Def: {self.defense}, Sp.Atk: {self.sp_attack}, Sp.Def: {self.sp_defense}, Speed: {self.speed}"

class Pokedex:
    def __init__(self, csv_file):
        self.pokemons = self.load_pokemons(csv_file)

    def load_pokemons(self, csv_file):
        pokemons = []
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pokemons.append(Pokemon(
                    row['pokedex_number'],
                    row['name'],
                    row['type_1'],
                    row['type_2'],
                    int(row['hp']),
                    int(row['attack']),
                    int(row['defense']),
                    int(row['sp_attack']),
                    int(row['sp_defense']),
                    int(row['speed'])
                ))
        return pokemons

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def modify_pokemon(self, pokedex_number, **kwargs):
        for pokemon in self.pokemons:
            if pokemon.pokedex_number == pokedex_number:
                for key, value in kwargs.items():
                    setattr(pokemon, key, value)
                break

    def remove_pokemon(self, pokedex_number):
        # Iterar a través de la lista de Pokémon usando una copia para modificar la lista original
	    for pokemon in self.pokemons[:]:
	        if pokemon.pokedex_number == pokedex_number:
	            self.pokemons.remove(pokemon)
	            return True
	    
	    # Si no se encuentra ningún Pokémon con ese número de Pokedex
	    return False

    def get_pokemon(self, pokedex_number):
        for pokemon in self.pokemons:
            if pokemon.pokedex_number == pokedex_number:
                return pokemon
        return None

    def battle(self, pokemon1, pokemon2):
        print(f"Batall entre {pokemon1.name} and {pokemon2.name}!")

        # Arte
        battle_ascii = """
        $$$$$$$   $$$$$  $$$$$$$$  $$$$$  $$       $$       $$$$$    $$ $$ $$  
        $$    $$ $$   $$    $$    $$   $$ $$       $$      $$   $$   $$ $$ $$ 
        $$$$$$$  $$$$$$$    $$    $$$$$$$ $$       $$      $$$$$$$   $$ $$ $$  
        $$    $$ $$   $$    $$    $$   $$ $$       $$      $$   $$       
        $$$$$$$  $$   $$    $$    $$   $$ $$$$$$   $$$$$$$ $$   $$   $$ $$ $$
        """
        print(battle_ascii)
        # Animar con puntos durante 10 segundos
        for _ in range(10):
	        time.sleep(1)
	        print("$$$$$$$$$$", end="", flush=True)
        print("\n")

        if pokemon1.speed > pokemon2.speed:
            winner = pokemon1 if pokemon1.attack > pokemon2.defense else pokemon2
        else:
            winner = pokemon2 if pokemon2.attack > pokemon1.defense else pokemon1
        print(f"El Ganador es {winner.name}!")

    def show_pokemon_card(self, pokedex_number):
        pokemon = self.get_pokemon(pokedex_number)
        if pokemon:
            print("\n--- Tarjeta de Pokémon ---")
            print(f"Nombre: {pokemon.name}")
            print(f"Tipo: {pokemon.type_1}/{pokemon.type_2}")
            print(f"HP: {pokemon.hp}")
            print(f"Ataque: {pokemon.attack}")
            print(f"Defensa: {pokemon.defense}")
            print(f"Ataque Especial: {pokemon.sp_attack}")
            print(f"Defensa Especial: {pokemon.sp_defense}")
            print(f"Velocidad: {pokemon.speed}")
            print("--------------------------\n")
        else:
            print("El Pokémon no existe.")

def main():
    pokedex = Pokedex('data/pokemon.csv')

    while True:
        print("\n--- Menú de Pokedex ---")
        print("1. Ver todos los Pokémon")
        print("2. Agregar un nuevo Pokémon")
        print("3. Modificar un Pokémon existente")
        print("4. Eliminar un Pokémon")
        print("5. Simular una batalla")
        print("6. Mostrar tarjeta de un Pokémon")
        print("7. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
        	# Mostrar Pokémon de 50 en 50
        	total_pokemon = len(pokedex.pokemons)
        	for i in range(0, total_pokemon, 50):
		        # Obtener el grupo actual (máximo 50 Pokémon)
		        current_group = pokedex.pokemons[i:i+50]
		        
		        print(f"\nMostrando Pokémon {i+1}-{min(i+50, total_pokemon)} de {total_pokemon}:")
		        for pokemon in current_group:
		            print(pokemon)
		        
		        # Si no es el último grupo, pedir al usuario que presione Enter
		        if i + 50 < total_pokemon:
		            input("\nPresione Enter para ver los siguientes 50 Pokémon...")

        elif choice == '2':
            if pokedex.pokemons:
                next_pokedex_number = max(int(pokemon.pokedex_number) for pokemon in pokedex.pokemons) + 1
            else:
                next_pokedex_number = 1
            print(f"El siguiente número disponible de la Pokédex es: {next_pokedex_number}")

            while True:
                pokedex_number = input("Número de Pokédex: ")
                if pokedex.get_pokemon(pokedex_number):
                    print("El número de Pokédex ya existe. Por favor, ingrese un número diferente.")
                else:
                    break

            name = input("Nombre: ")
            type_1 = input("Tipo 1: ")
            type_2 = input("Tipo 2: ")
            
            while True:
                try:
                    hp = int(input("HP: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para HP.")
            
            while True:
                try:
                    attack = int(input("Ataque: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para Ataque.")
            
            while True:
                try:
                    defense = int(input("Defensa: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para Defensa.")
            
            while True:
                try:
                    sp_attack = int(input("Ataque Especial: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para Ataque Especial.")
            
            while True:
                try:
                    sp_defense = int(input("Defensa Especial: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para Defensa Especial.")
            
            while True:
                try:
                    speed = int(input("Velocidad: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero para Velocidad.")
            
            nuevo_pokemon = Pokemon(pokedex_number, name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed)
            pokedex.add_pokemon(nuevo_pokemon)
            print("Pokémon agregado exitosamente.")

        elif choice == '3':
            pokedex_number = input("Número de Pokédex del Pokémon a modificar: ")
            name = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            hp = input("Nuevo HP (dejar en blanco para no cambiar): ")
            attack = input("Nuevo Ataque (dejar en blanco para no cambiar): ")
            defense = input("Nueva Defensa (dejar en blanco para no cambiar): ")
            sp_attack = input("Nuevo Ataque Especial (dejar en blanco para no cambiar): ")
            sp_defense = input("Nueva Defensa Especial (dejar en blanco para no cambiar): ")
            speed = input("Nueva Velocidad (dejar en blanco para no cambiar): ")

            kwargs = {}
            if name: kwargs['name'] = name
            if hp:
                try:
                    kwargs['hp'] = int(hp)
                except ValueError:
                    print("Por favor, ingrese un número entero para HP.")
            if attack:
                try:
                    kwargs['attack'] = int(attack)
                except ValueError:
                    print("Por favor, ingrese un número entero para Ataque.")
            if defense:
                try:
                    kwargs['defense'] = int(defense)
                except ValueError:
                    print("Por favor, ingrese un número entero para Defensa.")
            if sp_attack:
                try:
                    kwargs['sp_attack'] = int(sp_attack)
                except ValueError:
                    print("Por favor, ingrese un número entero para Ataque Especial.")
            if sp_defense:
                try:
                    kwargs['sp_defense'] = int(sp_defense)
                except ValueError:
                    print("Por favor, ingrese un número entero para Defensa Especial.")
            if speed:
                try:
                    kwargs['speed'] = int(speed)
                except ValueError:
                    print("Por favor, ingrese un número entero para Velocidad.")

            pokedex.modify_pokemon(pokedex_number, **kwargs)
            print("Pokémon modificado exitosamente.")

        elif choice == '4':
            pokedex_number = input("Número de Pokédex del Pokémon a eliminar: ")
            pokedex.remove_pokemon(pokedex_number)
            print("Pokémon eliminado exitosamente.")

        elif choice == '5':
            pokedex_number1 = input("Número de Pokédex del primer Pokémon: ")
            pokedex_number2 = input("Número de Pokédex del segundo Pokémon: ")
            pokemon1 = pokedex.get_pokemon(pokedex_number1)
            pokemon2 = pokedex.get_pokemon(pokedex_number2)
            if pokemon1 and pokemon2:
                pokedex.battle(pokemon1, pokemon2)
            else:
                print("Uno o ambos Pokémon no existen.")

        elif choice == '6':
            pokedex_number = input("Número de Pokédex del Pokémon: ")
            pokedex.show_pokemon_card(pokedex_number)

        elif choice == '7':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()