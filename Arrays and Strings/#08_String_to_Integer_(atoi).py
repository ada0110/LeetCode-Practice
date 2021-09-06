import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        max_INT = 2**31 - 1
        min_INT = -2**31
        # allowing only +, - and digits
        exp = r'[+-]?\d+'
        s = re.match(exp, s)
        # print(s.group())
        if s:
            num = int(s.group())
            if num > max_INT:
                return max_INT
            elif num < min_INT:
                return min_INT
            else:
                return num
        return 0 


s = Solution()
ans = s.myAtoi("  abc 42  ")
print(ans)