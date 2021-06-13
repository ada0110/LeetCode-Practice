'''
Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. It is guaranteed there is at 
least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Ex:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

'''
# import nltk
import re
from typing import List
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # converting to lowercase and removing , . or any extra characters
        # para= re.sub(r"[- _,.;!]", " ", paragraph.lower())
        # print("after removing , and .:", para1)
        # words = word_tokenize(para)

        m = {}
        para = paragraph
        s = " "
        
        for word in para:
            if word.isalpha():
                s += word.lower()
            else:
                s += " "
        print("string: ", s)

        words = s.split()
        print("words: ", words)

        # storing freq of each word in map
        for word in words:
            if word in m:
                m[word] += 1
            else:
                m[word] = 1
        print("old:", m)

        # removing banned word from map
        for bword in banned:
            if bword in m.keys():
                del m[bword]
        print("new:", m)


        # checking the most frequently occurred word
        max_freq = 0
        ans = " "
        for word, freq in m.items():
            if freq > max_freq:
                ans = word
                max_freq = freq
        return(ans)

s = Solution()
ans = s.mostCommonWord(paragraph= "Bob hit a ball, the hit BALL flew far  after it was hit.", banned=["hit"]) #"a, a, a, a, b,b,b,c, c", banned=["a"]
print(ans)