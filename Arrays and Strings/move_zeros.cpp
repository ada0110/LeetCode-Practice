#include<iostream>
using namespace std;


void moveZeroes(int* nums, int n)
{
    int j = 0;
    for(int i=0; i<n; i++)
    {
        if(nums[i]!=0)
        {
            nums[j] = nums[i];
            j += 1;
        }

    }
    for (int k=j; k<n; k++)
        nums[k] = 0;

    // printing the final array
    cout << "Final array is: ";
    for(int l=0; l<n; l++)
        cout << nums[l] << " ";
    
}

int main()
{
    int nums[100], n;
    cout <<"Enter the size of nums array:"<< endl;
    cin >> n;
    cout << "Enter " << n << " elems into nums arr: " << endl;

    for(int i=0; i<n; i++)
        cin >> nums[i];

    moveZeroes(nums, n);    

}