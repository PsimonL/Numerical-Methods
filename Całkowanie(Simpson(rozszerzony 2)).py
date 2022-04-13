import math
import numpy as np

def function(x):
    return ((x+1)/(x+2))

if __name__ == '__main__':
    print("ZLOZONA METODA SIMPSONA")
    a = 0
    b = 3
    n = 10
    h = (b - a) / n
    values = list(map(function, np.arange(a, b + 1, h)))
    counter = 0
    final_value = 0
    while counter + 2 < len(values):
        final_value += (values[counter] + 4 * values[counter + 1]
                        + values[counter + 2]) * h / 3
        counter += 2
    print(final_value)