from math import *

def function(x):
    return (sin(x))


if __name__ == '__main__':
    print("METODA SIMPSONA")
    a = int(input("Podaj poczatek przedzialu calkowania: a = "))
    b = int(input("Podaj koniec przedzialu calkowania: b = "))

    #temp = (b - a) / n
    h = ((a + b) / 2) - a
    print(h)
    integral = (function(a) + 4 * function((a + b) / 2) + function(b)) * h / 3
    print(integral)