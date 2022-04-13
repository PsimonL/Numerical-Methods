import math as m
import random as r
import numpy as np

def function(x):
    #return (10*(x-5)**5 + 3*(x-5)**2 + x + 3)
    return(10*(x-5)**5 + 3*(x-5)**2 + x + 3)

def golden_ratio_method(a, b, fxl, fxp):
    fi = 0.61803398 #liczba odwrotna do zlotej liczby ((sqrt(5) - 1) / 2)

    xl = b - fi * (b - a)
    xp = a + fi * (b - a)

    EPSILON = 0.0001 #dokladnosc zadana
    while (b - a) <= EPSILON:
        if fxl > fxp:
            a = xl
            xl = xp
            xl = b - fi * (b - a)
        elif fxl < fxp:
            b = xp
            xp = xl
            xp = a + fi * (b - a)
    score = (a+b) / 2
    return (score)


if __name__ == "__main__":
    while True:
        # [a, b] <- obustronnie domknięty przedział ciągłości
        """a = float(input("a = "))
        b = float(input("b = "))
        # xl i xp losowe wartosci z przedzialu gdzie xl < xp
        #xl = r.randint(1, 5)
        xl = float(input("xl = "))
        xp = float(input("xp = "))"""
        a = 0.1
        b = 9.31
        xl = 5.325
        xp = 8.74
        fxl = function(xl)
        fxp = function(xp)

        if a < xl < xp < b: #a < xl and xl < xp and xp < b
            print("Poprawnie zdefiniowano wartosci: " + str(a) + " < " + str(xl) + " < "
                  + str(xp) + " < " + str(b))
            print("Minimum istnieje dla puntu: x = " + str(golden_ratio_method(a, b, fxl, fxp)) + " i y = "
                  + str(function(golden_ratio_method(a, b, fxl, fxp))))
            break
        else:
            print("Wartosc nie zostala poprawnie zdefiniowana")
