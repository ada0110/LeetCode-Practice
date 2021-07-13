'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''

from typing import List

class Solution:

    def backtrack(self, ans, m, digits, combination, idx):
        if idx > len(digits):
            return
        
        if (len(digits) == len(combination)):
            ans.append(combination[:])
            return

        curr_digit = digits[idx]
        curr_str = m[curr_digit]

        for i in range(len(curr_str)):
            self.backtrack(ans, m, digits, combination + curr_str[i], idx+1)
 

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return
        
        # creating map for digits
        m = {}

        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"  

        self.backtrack(ans, m, digits, " ", 0)
        return ans





s = Solution()
ans = s.letterCombinations(digits="23")
print(ans)


