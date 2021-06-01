'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''


from typing import List

class Solution:
    
    # def findHash(self, s):
    #     return ''.join(sorted(s)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ans = []

        for s in strs:
            # print("str:", s)
            h_key = ''.join(sorted(s))
            # h_key = self.findHash(s)
            # print("sorted:", h_key)

            # if the sorted str is not present in map then we create an empty list as its value
            # this will get executed for all strings which are occuring for first time 
            # as the map won't have its instance 
            if h_key not in m:
                m[h_key] = []

            # if sorted str is present mean if we have already came across its anagram
            # then we simply append the given string as the value of sorted string
            m[h_key].append(s)

            # print(m)
            # {'ant': ['nat', 'tan'], 'aet': ['eat', 'tea', 'ate'], 'abt': ['bat']}

        # then we store the values which are anagrams into a list named ans  
        for value in m.values():
            ans.append(value)
        
        return ans



s = Solution()
ans = s.groupAnagrams(['nat', 'eat', 'tea', 'bat', 'ate', 'tan'])
print(ans)