'''
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1] * len(nums)
        postfix_mul = [1] * len(nums)

        prefix_mul[0] = nums[0]
        postfix_mul[len(nums)-1] = nums[-1]

        for i in range (1, len(nums)):
            prefix_mul[i] = prefix_mul[i-1] * nums[i]

        for i in range (len(nums)-1, 0, -1):
            # print("i:", i)
            postfix_mul[i-1] = postfix_mul[i] * nums[i-1] 
            # print(postfix_mul[i])
        prefix_mul.insert(0, 1)
        postfix_mul.append(1)

        print(f"prefix_mul: {prefix_mul}")
        print(f"postfix_mul: {postfix_mul}")

        output = [0] * len(nums)

        for i in range(0, len(nums)):
            print(f"prefix_mul[{i}]: {prefix_mul[i]} \
                    postfix_mul[{i+1}]:{postfix_mul[i+1]} : {prefix_mul[i] * postfix_mul[i+1]}")
            output[i] = prefix_mul[i] * postfix_mul[i+1]
            print(output)
        return output


s = Solution()
ans = s.productExceptSelf(nums = [2,3,4,5])
print(ans)