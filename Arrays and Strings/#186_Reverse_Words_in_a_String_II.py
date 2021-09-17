from typing import List

class Solution:

    def reverse(self, s, l, r):
    
        # reversing the list of words
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
    

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1

        # converting list of characters to a list of words
        s = (''.join(s)).split()
        print("before reversal:", s)

        # reversing the list of words
        s = self.reverse(s, l, r)
        print("after reversal:", s)

        # converting list of words to a string of words
        s = ' '.join(s)
        print(s)

        # converting string of words to list of characters
        s = [char for char in s]
        print(s)
        
        
    #   second version of code 
    def reverseWordsV2(self, s):
        l = 0
        r = len(s)-1
        # reverse the whole string
        self.reverse(s, l ,r)
        print("V2 after reversal:", s)
        
        # now again reverse the characters till space and then reverse another word and so on
        # reverse each word in a string
        
        for idx, char in enumerate(s):
            print(idx, char)
            if char == ' ':
                print("idx:", idx)
                self.reverse(s, l, idx-1)
                l = idx + 1
            # not able to reverse the last word so call separately for the last word
        self.reverse(s, l, r)
        print("s:", s)
        


        
s = Solution()
# ans = s.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
ans1 = s.reverseWordsV2(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])