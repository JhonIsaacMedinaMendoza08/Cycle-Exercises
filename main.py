#Escriba un programa que muestre una tabla de multiplicar como la siguiente:

print ("Exercise 4 Multiplication table")

for j in range (1, 11):
    for i in range (1, 11):
        print (i*j, end="\t")
    print()