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
        i = 1
        while (i<len(arr) and arr[i] > arr[i-1]):
            i += 1
        if (i==1 or i==len(arr)):
            return False
        while (i<len(arr) and arr[i] < arr[i-1]):
            i += 1
        
        return (i == len(arr))


s = Solution()
ans = s.validMountainArray([0,2,3,4,5,2,1])
print(ans)
