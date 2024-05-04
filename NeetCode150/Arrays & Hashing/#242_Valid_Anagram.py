'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol1
        d_s = {}
        for word in s:
            if word in d_s:
                d_s[word] += 1
                print(d_s)
            else:
                d_s[word] = 1

        print("d_s:", d_s)

        d_t = {}
        for word in t:
            if word in d_t:
                d_t[word] += 1
                print(d_t)
            else:
                d_t[word] = 1

        print("d_t:", d_t) 

        if d_s.items() == d_t.items():
            return True
        return False
    
    # sol2
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if Counter(s) == Counter(t):
            return True
        return False
    
    # sol3
    def isAnagramV2(self, s, t):
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        print(countS.items(),'\n', countT.items())
        if countS == countT:
            return True

        return False
    

s = Solution()
#ans = s.isAnagram("aarti", "raati")
ans = s.isAnagram("anagram", "nagaram")
print(ans)