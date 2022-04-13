import math
from numpy import *
from math import *

def function(x):
    return (sin(x))



if __name__ == '__main__':
    print("ZLOZONA METODA SIMPSONA")
    a = 1
    b = 4
    n = 10

    h = (b - a) / n

    if n % 2 == 0:
        pom1 = n / 2
    else:
        print("Wprowadziles nieparzysta.")

    integral = 0
    length = round(n/2)
    d = 1
    while d <= length:
        integral += (function((a)) + 4 * function(a + h) + function(a + h * 2))
        a += 2 * h
        d += 1
    integral = integral * (h / 3)
    print(integral)



