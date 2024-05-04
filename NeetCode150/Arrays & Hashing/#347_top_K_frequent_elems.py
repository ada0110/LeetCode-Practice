'''
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

'''

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= len(set(nums)):
            num_count = {}

            for num in nums:
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1

            print(num_count)

            # sort the dictionary in reverse order and return top k elements
            sorted_num_count = dict(sorted(num_count.items(), key=lambda item: item[1], reverse=True))
            print(sorted_num_count)

            # as dictionary cannot be slices so convert it to list and take out top k elems
            return list(sorted_num_count.keys())[:k]

        
        # sol 2
        if k > len(set(nums)):
            return 

        d = {}
        result = []
        for num in nums:
            if num not in d:
                d[num] = 1
            d[num] += 1

        # sorting the dict
        sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sorted_dict[i][0])

        return result
    

s = Solution()
ans = s.topKFrequent(nums = [1,1,1,2,2,2, 3, 4,4,4,4,4,4,4,4,4, 5,5,5], k = 5)
print(ans)
    