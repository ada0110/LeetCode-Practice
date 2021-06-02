'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
'''

from os import O_NDELAY
from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # creating a map to store summation of pairs and occurence 
        m = {}
        ans = 0
        # taking lists A and B and find sum for each elem in both lists  
        for i in range(len(A)):
            x = A[i]

            for j in range(len(B)):
                y = B[j]

                # calculating the sum
                sum_ = x + y

                # first checking whether x+y (sum_) is already present in dictionary, if not initialize its count as zero
                if (sum_ not in m):
                    m[sum_] = 0
                # storing the sum as key and its occurence as value in map
                m[sum_] += 1
        
        # looping over lists C and D to find sum as -(x+y) so that answer will be zero when added
        for i in range(len(C)):
            x = C[i]
            for j in range(len(D)):
                y = D[j]

                # setting target as -ve of (x+y)
                target = -(x+y)
                # now if the target is present in map then it means we have pairs, when added sum up to zero
                # so we take out its num of occurence by accesing its value
                # and add that to ans which will give number of tuples for which the sum was zero
                if target in m:
                    ans = ans + m[target]
        
        return ans



s = Solution()
ans_ = s.fourSumCount(A = [1,2], B = [-2,-1], C = [-1,2], D = [0,2])    
print(ans_)            

# A = [1,2]
# B = [-2,-1]
# C = [-1,2]
# D = [0,2]

# A[1] + B[1] + C[0] + D[0] = 0
# A[0] + B[0] + C[0] + D[1] = 0

