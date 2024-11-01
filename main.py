#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
#π=   4(1−13+15−17+…)

import math

print ("Exercise 8 PI")

def estimate_pi(number):
    addition = 0.0
    for j in range (number):
        term = math.pow(-1, j) / (2 * j + 1)
        addition = addition + term
    estimate_pi = 4 * addition
    return estimate_pi

number = int(input("Enter the number of terms (n):"))
answer = estimate_pi(number)
print (f"Estimation of π with {number} terms: {answer}")