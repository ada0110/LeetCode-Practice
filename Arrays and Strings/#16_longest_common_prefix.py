'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        for s in strs:
            print(list(s), len(s))
            if len(s) < min_len:
                min_len = len(s)
        print(min_len)
        
        res = ""
        for i in range(min_len):
            for s in strs:
                print(f"s:{s}\ni:{i}\ts[{i}]:{s[i]}\tstrs[0][{i}]:{strs[0][i]}")
                # iterating over each s and checking for letters from 0th positions to min_len
                if s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
            print("res:", res)
            print("\n")
        return res
            

s = Solution()
ans = s.longestCommonPrefix(strs = ["flower","flow","flight"])
print(ans)