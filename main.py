#Escriba un programa que entregue todos los divisores del número entero ingresado:


print ("Exercise 5 Dividers")

def get_dividers (number):
    dividers =[]
    for i in range (1, number + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers

number = int(input("Please, enter number: "))

dividers = get_dividers(number)
print("Los divisores de", number, "son:", " ".join(map(str, dividers)))


