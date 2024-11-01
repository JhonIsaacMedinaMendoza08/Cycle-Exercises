#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:


print ("Exercise 9 Addition of fractions")

def fractional_powers():
    pow = 1
    frac = 0.5
    addition = 0.0

    print(f"{'Pow':<10}{'Fracción':<10}{'addition':<10}")
    
    while frac > 0.000001:
        addition = addition + frac
        print(f"{pow:<10}{frac:<10}{addition:<10}")
        
        pow = pow + 1
        frac = frac / 2  

fractional_powers()