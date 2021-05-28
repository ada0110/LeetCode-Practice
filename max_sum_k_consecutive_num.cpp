#include<iostream>

using namespace std;

int maxSum(int* arr, int n, int k)
{
    if (n<k)
    {
        cout << "Invalid Operation";
        return -1;
    }

    // finding out sum of first window 
    int win_sum = 0;  
    for(int i=0; i<k; i++)
        win_sum = win_sum + arr[i];
    
    int max_sum = win_sum;
    // printf("%d", win_sum);

    // finding sum of remaining windows by removing element from prev window and 
    // adding next elem to current window
    for (int i=0; i<n-k; i++)
    {
        win_sum = win_sum - arr[i] + arr[i+k];
        max_sum = max(win_sum, max_sum); 
    }

    // can also be done as follows
    // for (int i=k; i<n; i++)
    // {
    //     win_sum += arr[i] - arr[i-k];
    //     max_sum = max(win_sum, max_sum);
    // }

    return max_sum;
    
}


int main()
{
    int arr[] = {80, -50, 90, 100};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = 2; //window size
    cout << maxSum(arr, n, k);
    return 0;
}