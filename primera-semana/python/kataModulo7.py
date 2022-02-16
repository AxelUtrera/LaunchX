#Kata modulo 7

#Ejercicio 1: Crear una aplicacion la cual pida al usuario ingrese el nombre de los planetas y los almacene en una lista.

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("write a new planet, write 'done' to exit... ")
    
#Escribe un ciclo while el cual muestre los nombres de los planetas ingresados por el usuario.

for planet in planets:
    print(planet)

