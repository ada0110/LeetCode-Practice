import re

class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # s = re.sub(' +', ' ', s).split()
        s = s.split()
        print(s, len(s))
        l = 0
        r = len(s)-1
        print(l,r)

        while l < r:
            # temp = s[l]
            # s[l] = s[r]
            # s[r] = temp
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        s = ' '.join([str(char) for char in s])
        return s

    def reverseWordsV2(self, s):
        s = s.split()
        return ' '.join(s[::-1])

    # def reverseWordsV3(self, s):
    #     s = s.split()
    #     print(s.reverse())


s = Solution()
ans = s.reverseWords('The     quick brown    fox')
print("ans:", ans)

# ans1 = s.reverseWordsV2('The     quick brown    fox')
# ans2 = s.reverseWordsV3('The     quick brown    fox')
# print("ans1:", ans1)
# print("ans2:", ans2)
# # ("    hello   world")


# import re
# re.sub(' +', ' ', 'The     quick brown    fox')
