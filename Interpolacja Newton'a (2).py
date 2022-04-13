from numpy import prod


class Punkt:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y


def policz(punkty, x):
    ilorazy = [[punkt.x, punkt.y] for punkt in punkty]
    for i in range(1, len(punkty)):
        for j in range(i, len(punkty)):
            ilorazy[j].append((ilorazy[j][i] - ilorazy[j - 1][i]) // (ilorazy[j][0] - ilorazy[j - i][0]))

    ilorazy = list(map(lambda x: x[len(x)- 1], ilorazy))
    print(sum([ilorazy[i] * prod(list(map(lambda y: x - y.x,punkty))[:i]) for i in range(len(ilorazy))]))



if __name__ == "__main__":
    policz([Punkt(-2, -1), Punkt(-1, 0), Punkt(0, 5), Punkt(2, 99), Punkt(4, -55)], 8)