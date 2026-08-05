#include <stdio.h>

void swap_double(double a[static 2]) {
    auto tmp = a[0];
    a[0] = a[1];
    a[1] = tmp;
}

int main(void) {
    double A[2] = { 1.0, 2.0, };
    swap_double(A);
    printf("A[0] = %g, A[1] = %g\n", A[0], A[1]);
}

double dot_product(
    const double *a,
    const double *b,
    size_t n)
{
    double sum = 0.0;
    for(size_t i = 0; i < n; i++)
        sum += a[i] * b[i];

    return sum;
}

void mat_vec_mul(
    size_t rows,
    size_t cols,
    double A[rows][cols],
    double x[cols],
    double result[rows])
{
    for(size_t i = 0; i < rows; i++)
    {
        result[i] = 0.0;

        for(size_t j = 0; j < cols; j++)
        {
            result[i] += A[i][j] * x[j];
        }
    }
}