#include <stdio.h>

void merge(int arr[], int left, int mid, int right)
{
   // create to int len for both left and right halfs
   int n1 = mid - left + 1;
   int n2 = right - mid;

   // create two arrs with left and right sizes
   int L[n1];
   int R[n2];

   for (int i = 0; i < n1; i++)
       L[i] = arr[left + i];

   for (int i = 0; i < n2; i++)
       R[i] = arr[mid + 1 + i];
    
   int i = 0;
   int j = 0;
   int k = left;

   while (i < n1 && j < n2)
   {
    if (L[i] <= R[j])
       arr[k++] = L[i++];
    
    else
       arr[k++] = R[j++];
       
   }

   while (i < n1)
       arr[k++] = L[i++];
    
   while (j < n2)
       arr[k++] = R[j++];

}


void merge_sort(int arr[], int left, int right)
{
    if (left >= right)
        return;
    
    int mid = left + (right - left) / 2;

    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);

    merge(arr, right, mid, left);
}


/* Why Merge Sort */
/*
Guaranteed O(n log n)
Stable sort
Good for linked lists and external sorting
Requires extra memory O(n)
*/


void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = *a;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];

    int i = low - 1;

    for (int j = low; j < high; j++)
    {
       if (arr[j] < pivot)
       {
        i++;
        swap(&arr[i], &arr[j]);
       }
    }
    
    swap(&arr[i + 1], &arr[high]);

    return i + 1;
}

void quick_sort(int arr[], int low, int high)
{
    if (low >= high)
       return;
    
    int p = partition(arr, low, high);

    quick_sort(arr, low, p - 1);
    quick_sort(arr, p + 1, high);
}


/* Why Quick Sort? */
/* 
Average O(n log n)
In-place sorting
Better cache locality
Usually faster in practice
Worst case O(n²)
*/