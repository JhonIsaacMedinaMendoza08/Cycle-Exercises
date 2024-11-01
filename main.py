#Desarrolle un programa que entregue la secuencia de Collatz de un número entero:

print ("Exercise 11  Collatz sequence")

def Sequence_collatz(number):
    Sequence = []  
    while number != 1:
        Sequence.append(number)  
        if number % 2 == 0:
            number //= 2  
        else:
            number = 3 * number + 1  
    Sequence.append(1)  
    return Sequence

number = int(input("Enter an integer: "))
answer = Sequence_collatz(number)

print(" ".join(map(str, answer)))