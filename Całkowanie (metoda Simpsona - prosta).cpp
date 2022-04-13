#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
using namespace std;

double function(double x)
{
    return (2*x*x+2*x+ 2);
}

double simpsonIntegral(double x_0, double x_n)
{
    double h = (x_n - x_0) / 2;
    return(function(x_0) + 4*function((x_n + x_0)/2) + (function(x_n))) * (h / 3);
}

double extendedsimpsonIntegral(double x_0, double x_n, double n)
{
    double h = (x_n - x_0) / n;
    double I = 0;
    for (int i = 1; i <= n / 2; i++)
    {
        I += (function(x_0) + 4 * function(x_0 + h) + function(x_0 + h * 2)) ;
        x_0 += 2 * h;
    }
    I *= (h/3);
    return I;
}

double random(double x_0, double x_n)
{
    double x = x_0 + static_cast<double>(rand()) / (static_cast<double>(RAND_MAX / (x_n - x_0)));
    return x;
}

double monteCarlo(double x_0, double x_n, double n)
{
    double sum = 0;
    for (int i = 0; i < n; i++) sum += function(random(x_0, x_n))/n;
    sum = sum * abs(x_n - x_0);
    return sum;
}

int main()
{
    int n, x_0, x_n;
    cout << "Enter x_0: ";
    cin >> x_0;
    cout << "Enter x_n: ";
    cin >> x_n;
    cout << "Enter n: ";
    cin >> n;
    cout << endl;
    //cout << "Simpson integral: " << simpsonIntegral(x_0, x_n) << endl;
    cout << "Extended Simpson integral: " << extendedsimpsonIntegral(x_0, x_n, n) << endl;
    //cout << "Monte Carlo integral: " << monteCarlo(x_0, x_n, n) << endl;
}