'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

d = { 
    'I':1, 
    'V':5, 
    'X':10, 
    'L':50, 
    'C':100, 
    'D':500, 
    'M':1000
    }

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        
        # for i in range(len(s)-1):
        while i < len(s):
            # if the literals are in decreasing order, subtraction case
            if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]] 
                i += 2
            else:
                ans += d[s[i]]
                i += 1

        return ans
       

s = Solution()
ans = s.romanToInt("MCMX")
print(ans)