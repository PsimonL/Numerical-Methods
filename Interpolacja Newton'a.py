if __name__ == "__main__":
    listX = [2, 52, 152]
    listY = [4, 54, 154]

    #1.94591 , 2.19722
    """listX = []
    listY = []"""

    n = int(input("Liczba znanych nam punktow: "))
    arg = int(input("Prosze wprowadzic argument dla ktorego chcesz znalezc wartosc: "))
    #print("Prosze wprowadzic kolejno wszystkie punkty: ")

    """for i in range(n):
        x = int(input("Podaj argument dla " + str(i + 1) + " punktu: "))
        y = int(input("Podaj wartosc dla " + str(i + 1) + " punktu: "))
        listX.append(x)
        listY.append(y)"""

    i = 0
    while i < n - 1:
        j = n - 1
        while i < j:
            listY[j] = (listY[j] - listY[j - 1]) / (listX[j] - listX[j - i - 1])
            j -= 1
        i += 1

    val = 0
    j = n - 1
    while j >= 0:
        temp = 1
        i = 0
        while i < j:
            temp *= (arg - listX[i])
            i += 1
        temp *= listY[i]
        val += temp
        j -= 1

    print("Wartosc szukana dla argumentu x = ", arg, " to y = ", val)
