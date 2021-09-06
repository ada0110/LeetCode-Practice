class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        ans = 0
        m = {}

        while left < n and right < n:

            # take the chara from string 
            chara = s[right]

            # if the chara already exists in map means we have already seen it
            # so we have to skip the prev entry and move the left pointer so that 
            # we don't take the chara twice. 
            if chara in m:
                left = max(left, m[chara]+1)
            
            # if not present in map, add to map 
            m[chara] = right
            ans = max(ans, right-left+1)
            right += 1 

        return ans



s = Solution()
ans = s.lengthOfLongestSubstring("")
print(ans)


# test cases
# abaaaacdaaa
# abaacad
# a
# ""
# """"