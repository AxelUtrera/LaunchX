#Kata modulo 9

#En este ejercicio, construirás un informe de combustible que requiere información de varias ubicaciones 
#de combustible en todo el cohete.

def gas_report(principal_tank, secundary_tank, emergency_tank):
    return f'''
        Average of gas in the starship:
        total average: {average(principal_tank, secundary_tank, emergency_tank)}%
        porcent of gas in tanks:
        principal tank: {principal_tank}%
        secundary tank: {secundary_tank}%
        emergency tank: {emergency_tank}%
    '''


def average(deposit1, deposit2, deposit3):
    average = (deposit1 + deposit2 + deposit3) / 3
    return average


print(gas_report(1000,35000,2000))


#Ejercicio2

def mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """

print(mission_report(14, 51, "Moon", 200000, 300000))

# Escribe tu nueva función de reporte considerando lo anterior


def mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """


print(mission_report("Moon", 10, 15, 51, main=300000, external=200000))

# Escribe tu nueva función

def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report 

print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))
