#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.


print ("Exercise 6 Travel time")

total_minutes = 0

while True:
    distance = int(input("travel time (0 to end): "))
    if distance == 0:
        break
    total_minutes = total_minutes + distance

hours = total_minutes // 60
minutes = total_minutes % 60

print (f"total travel time {hours}:{minutes:02d} hours")


