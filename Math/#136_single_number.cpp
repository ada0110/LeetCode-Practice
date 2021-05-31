/*Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Ex:
Input: nums = [4,1,2,1,2]
Output: 4
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void singleNumber(vector<int> &nums)
{
    int arr_sum = 0;

    // finding out the sum of all numbers in vector 
    for(int i=0; i<nums.size(); i++)
        arr_sum = arr_sum + nums[i];
    printf("arr_sum: %d\n", arr_sum);


    // finding sum of unique elems from vector using unique function
    // first sort the vector
    vector<int>:: iterator ip;
    std::sort(nums.begin(), nums.end());
    // we get [1,1,2,2,4,4,5]


    // now try to get unique elements
    ip = std::unique(nums.begin(), nums.begin()+7);
    // But we need to resize the vector as the size is same with undefined terms
    nums.resize(std::distance(nums.begin(), ip));


    // finding the sum of this unique vector
    int uniq_sum = 0;
    for(int j=0; j<nums.size(); j++)
        uniq_sum = uniq_sum + nums[j];
    printf("uniq_sum: %d\n", uniq_sum);


    // now the difference between 2*uniq_sum and arr_sum will be the single elem
    printf("single elem in array is: %d", 2*uniq_sum-arr_sum);
}
    

int main()
{
    vector<int> v1{4,1,2,1,2,4,5};
    singleNumber(v1);
    // dispAns(v1);
}