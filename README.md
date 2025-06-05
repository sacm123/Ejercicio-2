# Ejercicio-2
Pokédex Interactiva con Sistema de Batallas

Este proyecto simula una Pokédex interactiva que permite: ✅ Gestionar Pokémon (agregar, modificar, eliminar). ✅ Simular batallas entre Pokémon. ✅ Visualizar estadísticas detalladas de cada Pokémon.

pokedex/
│
├── data/
│ └── pokemon.csv # Base de datos de Pokémon (requerido)
│
├── main.py # Programa principal
└── README.md # Documentación

#Cómo Ejecutarlo

Clonar/descargar el repositorio y colocar el archivo pokemon.csv en data/.

Instalar Python (si no lo tienes).

Ejecutar el programa: python main.py

Menú Principal Opción Acción 1 Ver todos los Pokémon (paginados de 50 en 50). 2 Agregar un nuevo Pokémon (autogenera el número de Pokédex). 3 Modificar un Pokémon existente (actualiza stats). 4 Eliminar un Pokémon por su número de Pokédex. 5 Simular una batalla entre dos Pokémon. 6 Mostrar tarjeta detallada de un Pokémon. 7 Salir del programa.

Sistema de Batallas
Mecánica:

El Pokémon con mayor velocidad ataca primero.
Gana el que tenga mayor ataque que la defensa del rival.

Efectos visuales:
Animación con arte ASCII y puntos de carga (10 segundos).
