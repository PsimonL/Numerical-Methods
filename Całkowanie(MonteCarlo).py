import random
from numpy import *
from math import *

def function(x):
    return (sin(x))

if __name__ == "__main__":
    print("METODA MONTE-CARLO")
    a = int(input("Podaj poczatek przedzialu calkowania: a = "))
    b = int(input("Podaj koniec przedzialu calkowania: b = "))
    n = int(input("Podaj liczbe punktow z przedzialu calkowania: "))

    random_list = []
    for i in range(n):
        random_list.append(round(random.uniform(a, b), 2))
    #print(random_list)
    #random_list = [1.5, 2.6, 3.8, 4.5]

    average_value = 0
    for i in range(n):
        value = function(random_list[i]) / n
        average_value += value
    print(average_value)

    integration = average_value * abs(b - a)
    print(integration)