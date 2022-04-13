def function(x):
    val_for_x = (x * x * x) + 2
    return val_for_x


if __name__ == '__main__':
    print("Metoda trapezow - calkowanie: ")
    xp = int(input("Wprowadz poczatek przedzialu calkowania: "))
    xk = int(input("Wprowadz koniec przedzialu calkowania: "))
    n = int(input("Wprowadz liczbe czesci na ktora chcesz podzielic obszar calkowania: "))

    dx = (xk - xp) / n

    area = 0
    """for i in range(xp, n + 1, 1):
        area += function(xp + i * dx)
        area = (area + (function(xp) + function(xk)) / 2) * dx"""

    summary = 0.5 * (function(xp) + function(xk))
    for i in range(1, n):
        summary += function(xp + i * dx)

    area = dx * summary

    print("Wartosc calki metoda trapezow wynosi: ", end=" ")
    print(area)
