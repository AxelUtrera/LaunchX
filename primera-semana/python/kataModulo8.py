#Kata modulo 8
#Ejercicio 1: crea un diccionario que almacene informacion sobre el planeta marte

planet = {
    'name' : 'Mars',
    'moons' : 2
}

# Muestra el nombre del planeta y el número de lunas que tiene.

print("{} have {} moons".format(planet['name'], planet['moons']))

# Agrega la clave circunferencia con los datos proporcionados previamente
planet['circunferency (km)'] = {
    'polar' : 6752, 
    'equatorial' : 6792
}

# Imprime el nombre del planeta con su circunferencia polar.
print("{} have {} km of polar circunferency".format(planet['name'], planet['circunferency (km)']['polar']))


# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.
# Agrega el código para contar el número de lunas.
total_moons = 0
for moons in planet_moons.values():
    total_moons += moons
    
print("Total of moons:", total_moons)




