from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # sol1 
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1 

        for key, val in d.items():
            if val > 1:
                return True  
        return False

        # sol2
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = 1
        return False

        # sol3
        d = defaultdict(int)
        for num in nums:
            if d[num]:
                return True
            d[num] = 1
        return False

        # sol4
        if len(set(nums)) != len(nums):
            return True
        return False



s = Solution()
ans = s.containsDuplicate([1,2,3,1])
#print("printing ans: ")
print(ans)