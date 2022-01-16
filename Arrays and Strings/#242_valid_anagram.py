from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # most_common does not sort by keys even if values are same 
        # it maintains original order of keys so use sorted()
        # s =  "bbbaaaccc" t ="cccbbbaaa" without sorted it will fail

        # s_count = (Counter(s).most_common())
        # c_count = (Counter(t).most_common())

        # print(s_count, c_count)

        if Counter(s) == Counter(t):
            return True
        return False


    def isAnagramV2(self, s, t):
        countS = {}
        countT = {}

        for i, char in enumerate(s):
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1

        for i, char in enumerate(t):
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        print(countS.items(), countT.items())
        if countS == countT:
            return True
        return False

        print(countS, countT)   
        # won't work as iterating through only countS 
        # have to iterate through countT as well to work
        for key in countS:
            if countS[key] != countT.get(key, -1):
                return False
        return True


    def isAnagramV3(self, s, t):
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        print(countS.items(),'\n', countT.items())
        if countS == countT:
            return True

        return False
    


s = Solution()
# ans = s.isAnagramV2( "bbbaaaccc", "cccbbbaaa") #"anagram", "nagaram") #s="rat", t = "car") #
# print(ans)

ans2 = s.isAnagramV3( "bbbaaaccc", "cccbbbaaa")
print(ans2)

