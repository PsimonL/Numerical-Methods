import math
import numpy

def function(x):
    return ((x+1)/(x+2))


if __name__ == '__main__':
    a = 4
    b = 10
    n =
    print("Poczatek przedzialu calkowania: a = " + str(a))
    print("Koniec przedzialu calkowania: b = " + str(b))
    print("Liczba przedzialow calkowania - musi byc parzysta: n = " + str(n))

    h = 1

    if n % 2 == 0:
        pom1 = n / 2
    else:
        print("Wprowadziles nieparzysta.")

    list_of_args = []
    for j in range(a, b + 1):
        list_of_args.append(j)
    print(list_of_args)

    list_of_values = [None for _ in range(n + 1)]
    for g in range(len(list_of_args)):
        list_of_values[g] = function(list_of_args[g])
    print(list_of_values)

    if len(list_of_args) >= 5:
        final_list = [None for _ in range(len(list_of_args))]
        print(final_list)
        length = n/2
        k = 0
        help = 2
        while k <= length+help: # TU NIE DZIALA LICZBA ITERACJI, WRAZ Z WIĘKSZYMI PRZEDZIALAMI
                            #GORNYMI NALEZY DODAWAC +1 DO ITERACJI
            final_list[k] = (list_of_values[k] + 4 * list_of_values[k + 1]
                             + list_of_values[k + 2]) * h / 3
            k += 2
        print(final_list)
        print(sum(filter(None, final_list)))

    elif len(list_of_args) == 3:
        final_list = [None for _ in range(1)]
        for k in range(0, 1, 1):
            final_list[k] = (list_of_values[k] + 4 * list_of_values[k + 1]
                             + list_of_values[k + 2]) * h / 3
        print(final_list)
        print(sum(filter(None, final_list)))
