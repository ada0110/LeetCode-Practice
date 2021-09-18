from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = sorted(Counter(s).elements())
        c_count = sorted(Counter(t).elements())
        # print(s_count, c_count)

        if s_count == c_count:
            return True
        return False


s = Solution()
ans = s.isAnagram( s="rat", t = "car") #("anagram", "nagaram")
print(ans)