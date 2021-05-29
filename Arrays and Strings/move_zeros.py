'''283. Move Zeroes'''
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         j = 0
#         for num in nums:
#             if (num != 0):
#                 nums[j] = num
#                 j += 1
            
#         for x in range(j, len(nums)):
#             nums[x] = 0

def moveZeroes(nums):
    j = 0
    for num in nums:
        print(num)
        if (num != 0):
            nums[j] = num
            j += 1
        
    for x in range(j, len(nums)):
        nums[x] = 0

    print("Final array of nums:", nums)


nums = [0, 1, 3, 0, 12]
moveZeroes(nums)