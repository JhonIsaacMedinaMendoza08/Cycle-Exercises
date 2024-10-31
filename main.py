#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.



print ("Exercise 3 Addition between numbers")

number1 = int(input("Please, enter number: "))
number2 = int(input("Please, enter number: "))

if number1 > number2:
    number1, number2 = number2, number1

Addition = 0

for i in range (number1 + 1, number2):
    Addition += i
print (f"{Addition}")

