def interpolation(listX, listY, x, n):
    list_pom = []

    for k in range(n):
        list_pom.append(1)

    for i in range(n):
        for j in range(n):
            if i != j:
                list_pom[i] *= (x - listX[j])/(listX[i] - listX[j])

    print(list_pom)

    val = 0
    for a in range(n):
        val += listY[a] * list_pom[a]

    print("Szukana wartosc funkcji w argumencie x = ", x, "jest rowna y = ", val)


if __name__ == '__main__':
    numberOfPoints = int(input("Podaj liczbe argumentow dla ktorych znasz wartosci: "))
    valueInCertainArgument = int(input("Podaj argument dla ktorego chcesz znalezc wartosc: "))

    list_of_args = []
    list_of_vals = []

    for i in range(numberOfPoints):
        x = int(input("Podaj argument dla " + str(i + 1) + " punktu: "))
        y = int(input("Podaj wartosc dla " + str(i + 1) + " punktu: "))
        list_of_args.append(x)
        list_of_vals.append(y)
        #list_of_points.append((x,y))

    """print("X: ")
    print(list_of_args)
    print("Y: ")
    print(list_of_vals)"""

    interpolation(list_of_args, list_of_vals, valueInCertainArgument, numberOfPoints)