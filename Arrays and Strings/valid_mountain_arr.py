# 941. Valid Mountain Array
'''
Given an array of integers arr, return true if and only if it is a 
valid mountain array.

Recall that arr is a mountain array if and only if:

i) varr.length >= 3
ii) There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

'''

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr)<3):
            return False
        
        i = 1
        # checking for increasing subarray on left
        while (i<len(arr) and arr[i] > arr[i-1]):
            i += 1
        # if no increasing or no decreasing sequence in array    
        if (i==1 or i==len(arr)):
            return False
         # checking for decreasing subarray on right
        while (i<len(arr) and arr[i] < arr[i-1]):
            i += 1
         # if we obtain a mountain then return true
        return (i == len(arr))

# creating instance of a class
s = Solution()

# calling the method with given array 
ans = s.validMountainArray([0,2,3,4,5,2,1])
print(ans)
