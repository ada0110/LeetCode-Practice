class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        if x[0] == '-':
            x_rev = list(reversed(x[1:]))
            x_rev.insert(0, '-')
        else:
            x_rev = list(reversed(x))

        rev_int = int(''.join(x_rev))
        if rev_int > 2**31-1 or rev_int < -2**31:
            return 0
        else:
            return rev_int




s = Solution()
ans = s.reverse(-123)
print(ans)