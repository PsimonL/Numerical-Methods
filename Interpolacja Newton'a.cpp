#include<iostream>
#include<conio.h>

using namespace std;

void interpolation(double listX[], double listY[], int n, double arg){
    int i, j;
    for (i = 0; i < n; i++) {
        cout << "Argument dla " << i+1 << " punktu: ";
        cin >> listX[i];
        cout << endl;
        cout << "Wartosc dla " << i+1 << " punktu: ";
        cin >> listY[i];
    }

    double temp;
    double vals = 0;
    for(j = 0; j < n-1; j++) {
        for(i = n-1; j < i; i--) {//j<i
            listY[i] = (listY[i] - listY[i - 1]) / (listX[i] - listX[i - j - 1]);
        }
    }

    for(i = n-1; i >= 0; i--) {
        temp = 1;
        for(j=0; j < i; j++) {
            temp *= (arg - listX[j]);
        }
        temp *= listY[j];
        vals += temp;
    }
    cout << "\nWartosc szukana dla argumentu x = " << arg << " to  y = " << vals;
}

int main() {
    int n;
    double arg;

    cout << "Liczba znanych nam punktow: ";
    cin >> n;
    cout << endl;
    cout << "Prosze wpisac kolejno wszystkie punkty.\n";
    cout << "Wprowadz argument dla jakiego chcesz policzyc wartosc: ";
    cin >> arg;

    /*
     double listX[5] = {-2, -1, 0, 2, 4};
    double listY[5] = {-1, 0, 5, 99, -55};
     */

    auto* listX = new double[n]; //double
    auto* listY = new double[n]; //double

    interpolation(listX, listY, n, arg);

    return 0;
}