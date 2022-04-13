
#include <iostream>

using namespace std;

void Lab2(int n, double* x, double* y, double szukana) {
    double* l = new double[n], result = 0;

    for (int q = 0; q < n; q++) {
        l[q] = 1;
    }

    for (int q = 0; q < n; q++)
        for (int w = 0; w < n; w++)
            if (q != w)
                l[q] *= (szukana - x[w]) / (x[q] - x[w]);

    for (int q = 0; q < n; q++) {
        cout << l[q] << endl;
    }


    for (int q = 0; q < n; q++) {
        result += y[q] * l[q];
    }

    cout << "Wartosc funkcji w punkcie x=" << szukana << " jest rowna y="
         << result << "\n";
}

int main()
{
    cout << "Podaj liczbe punktow, dla ktorych sa znane wartosci oraz wartosc dla ktorej chcesz szukac: \n";
    int n, szukana;
    cin >> n >> szukana;
    double* x = new double[n];
    double* y = new double[n];

    for (int q = 0; q < n; q++) {
        cout << "Podaj kolejno punkt i jego wartosc dla wezla nr." << q + 1 << "\n";
        cin >> x[q] >> y[q];
    }

    Lab2(n, x, y, szukana);
    system("pause");
    return 0;
}