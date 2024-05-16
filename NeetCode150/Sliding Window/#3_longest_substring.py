'''
Given a string s, find the length of the longest 
substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = ''.join(s.split())
        print(s)
        l = 0
        r = l + 1
        max_len = 0
        
        if len(set(s)) == 1:
            return 1
        
        while (l < r):
            print(f"s[l]:{s[l]}\t s[r]:{s[r]}")
            if s[l] == s[r]:
                l += 1
            
            curr_len = r - l + 1
            max_len = max(curr_len, max_len)
            print(f"curr_len:{curr_len}\tmax_len:{max_len}\n")
            r += 1
            
        return max_len
    
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        l = 0
        max_len = 0
        char_set = set()
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            # print("char_set:", char_set)
            # print(max_len, r-l+1)
            max_len = max(max_len, r-l+1)
        
        return max_len
    
        
        
s = Solution()
ans = s.lengthOfLongestSubstring_v2(s = "abcabcbb")
print(ans)