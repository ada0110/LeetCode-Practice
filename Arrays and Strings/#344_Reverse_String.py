from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # initializing left and right pointers
        l = 0
        r = len(s)-1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1

        return s 

s = Solution()
ans = s.reverseString( ["H","a","n","n","a","h"])
print(ans)