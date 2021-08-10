import re
from collections import deque

def isPalindrome(s):
        # s = s.replace(" ", "").replace(",", "").replace(":", "").lower()
        s = s.lower()
        s = re.sub('[^a-z0-9]+', "", s)
        print(s)
        d = deque()
        for chara in s:
            d.append(chara)
        print(d)

        if len(d) == 1:
            return True

        while len(d) > 1:
            first = d.popleft()
            last = d.pop()

            if first != last:
                return False
        return True
    

# test cases
'''
"A man, a plan, a canal: Panama"
"race a car"
"i am aarti"
"A"
"%"
"pP"
"m-a-d-a-m"
"aCa"
"My name is *Aaarti*"
"10 01 10 01"
"1-0-1"
'''

ans = isPalindrome("madam")
print(ans)
