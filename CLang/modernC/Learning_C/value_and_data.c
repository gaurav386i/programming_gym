#include <stdio.h>
#include<complex.h>


double complex derivative(
    double complex (*F)(double complex),
    double complex z)
{
    const double h = 1e-6;
    return (F(z + h) - F(z)) / h;
}

double complex square(double complex z)
{
    return z * z;
}

int main(void)
{
    double complex z = 1.0 + 2.0 * I;

    double complex d = derivative(square, z);

    print("Derivatives = %.6f + %.6fi\n",
        creal(d),
        cimag(d));

    return 0;
}