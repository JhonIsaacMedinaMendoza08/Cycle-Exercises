#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos 
# consecutivos sea menor que 0,0001.


print ("Exercise 10 e ")

def Approx_e():
    addition = 1.0  
    number = 1
    term = 1 

    while True:
        term = term / number  
        if term < 0.0001:
            break
        addition = addition + term
        number = number + 1

    return addition

answer = Approx_e()
print(f"Approximation of e: {answer:.5f}")    