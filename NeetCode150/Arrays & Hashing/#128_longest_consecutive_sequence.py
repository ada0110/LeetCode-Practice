'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
                
        print(nums)
        
        for num in nums:
            # check if given num is start of a sequence
            if (num-1) not in nums_set:
                length = 0
                # as num has no left so keep checking whether next consecutive elems is in set 
                # and update the length 
                while (num + length) in nums_set:
                    length += 1
                longest_seq = max(longest_seq, length)
            
        return longest_seq
             
            
                
        # return ans 
    


s = Solution()
ans = s.longestConsecutive(nums=[9,1,4,7,3,-1,0,5,8,-1,6])
print(ans)