#include<iostream>
#include<math.h>

#define f(x) ((x*x*x) + 2)

using namespace std;
int main() {
    float a, b, integration=0.0, step, k;
    int i;
    const int subInterval = 4;


    cout << "Podaj poczatek przedzialu calkowania\n\n"
            "a = ";
    cin >> a;
    cout << "\nPodaj koniec przedzialu calkowania\n\n"
            "b = ";
    cin >> b;

    step = (b - a) / subInterval;

    integration = f(a) + f(b);

    for(i = 1; i <= subInterval-1; i++) {
        k = a + i * step;
        if(i % 2 == 0) {
            integration = integration + 2 * (f(k));
        } else {
            integration = integration + 4 * (f(k));
        }
    }

    integration = integration * step / 3;

    cout << endl << "Value of integration is: "<< integration;

    return 0;
}