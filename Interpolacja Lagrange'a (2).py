def count_i(x_vals, val):

    i_vals = []
    j = 1
    k = len(x_vals) - 1
    for i in range(len(x_vals)):

        if j > len(x_vals)-1:
            j = 0
        if k > len(x_vals)-1:
            k = 0

        first = (val - x_vals[j]) / (x_vals[i] - x_vals[j])
        second = (val - x_vals[k]) / (x_vals[i] - x_vals[k])

        i_value = (first, second)
        i_vals.append(i_value)

        j += 1
        k += 1

    return i_vals


def calculate_value(y_vals, i_vals):

    result = 0

    for i in range(len(y_vals)):
        result += y_vals[i] * i_vals[i]
    return result


if __name__ == '__main__':
    x = [1, 3, 5]
    y = [12, 4, 4]

    print(calculate_value(y, count_i(x, 4)))