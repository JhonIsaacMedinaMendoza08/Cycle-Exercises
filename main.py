#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

print ("Exercise 1 Multiples")

number = int(input("Please, enter number: "))

for i in range (1, 11):
    answer = number * i
    print (f"{number} * {i} = {answer}")