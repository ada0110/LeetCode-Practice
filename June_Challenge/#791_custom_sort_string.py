'''
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match
 the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Note:
order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.

'''

from collections import defaultdict

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        m = defaultdict(lambda : 30)

        for idx, char in enumerate(order):
            m[char] = idx
        
        # print(m)

        return "".join(sorted(list(string), key=lambda char:m[char]))
        #                   string = [a, b, c, d, e]  --> [2, 1, 0, 30, 30] --> [0, 1, 2, 30, 30] --> [c, b, a, d, e] or [c, b, a, e, d]
                  
s = Solution()
ans = s.customSortString(order = "cba", string = "adbce")
print(ans)


'''
order = "cba"
str = "abcd"

map : {c:0, b:1, a:2}
key = 
'''

