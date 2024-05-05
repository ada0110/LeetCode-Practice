'''
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # for both sol1 and sol2: The space complexity is also O(n) 
        # re.sub() function creates a new string with non-alphanumeric characters removed
        '''
        # O(n) space
        s = re.sub(r'[^0-9a-z]+', '', s.lower()) 
        print("s_clean:", s)
        
        # sol1 | O(n) time as creates a reversed copy of the string and O(n) space cz of re.sub() 
        if s[:] == s[::-1]:
            return True
        else:
            return False
        
        # sol2 | time complexity is O(n/2) = O(n)and O(n) space cz of re.sub()
        for i in range(len(s)//2):
            # print(f" if {s_clean[i]} == {s_clean[(len(s_clean)-1)-i]}")
            if s[i] == s[(len(s)-1)-i]:
               continue
            else:
                return False
        return True
            
        '''
        
        # sol3 | O(n) time and O(1) space :)
        # make use of l and r pointers and compare while (l<r)
        #  skip the non-apphanumeric characters using ascii values
        
        
        s = [c.lower() for c in s if self.is_alphanumeric(c)]
        l= 0
        r = len(s) - 1
        
        while (l < r):
            # print(f"begining of while l:{l}\tr:{r}")
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
                continue    
        return True
        
     
        
    def is_alphanumeric(self, s):
        for c in s:
            if (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or 
                ord('0') <= ord(c) <= ord('9')):
                return True
                 
            
        
            
s = Solution()
ans = s.isPalindrome(s = "A man, a plan, a canal: Panama")
print(ans)