'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # building hashmap of chara and number of times it has occurred
        c = Counter(s)
        # print(c)
        for i, chara in enumerate(s):
            if c[chara] == 1:
                return i 
            
        return -1



s = Solution()
ans = s.firstUniqChar("leetcode")
print(ans)
