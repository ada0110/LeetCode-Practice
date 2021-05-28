#include <iostream>

using namespace std;


int binarySearch(int* arr, int l, int r, int target)
{
    
    while (l<= r)
    {
        int mid = (l+r)/2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            return(binarySearch(arr, mid + 1, r, target));
        else
            return (binarySearch(arr, l, mid - 1, target));
    }
    
    return -1;
    
}

int main()
{
    int arr [] = {5, 8, 11, 15, 19, 25};
    int len = (sizeof(arr)/sizeof(arr[0]));
    int l = 0;
    int r = len - 1;
    int target = 15;
    int result =  binarySearch(arr, l, r, target);
    
    if (result != -1)
        printf("Element is present at index %d", result);
    else
        printf("The element does not exit in array.");
    
}