'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

** some solutions **

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = ['N']
#         m = {')':'(',']':'[','}':'{'}
#         for i in s:
#             if i in m.keys():
#                 if stack.pop() != m[i]:
#                     return False
#             else:
#                 stack.append(i)
                
#         return len(stack) == 1

'''

# Test Cases
"(])"
"(][)"
"{{}"
"[{}]"
"]"
"]["
"{[][][}"
"("
"{}]["
# MY SOLUTION

class Solution:
    def isMatch(self, s1, s2):
        if s1 == '(' and s2 == ')':
            return True
        elif s1 == '[' and s2 == ']':
            return True
        elif s1 == '{' and s2 == '}':
            return True
        else:
            return False
        
    def isValid(self, s: str) -> bool:
        # print(s)
        st = []
        for chara in s:
            # print("chara:", chara, end = '\n')
            if chara in ['(', '[', '{']:
                st.append(chara)
                # print("stack:", st)
                
            else:
                if len(st) > 0:
                    top = st[-1]
                    # print(top, chara)
                    ans = self.isMatch(top, chara)
                    if ans == True:
                        st.pop()
                    else:
                        return False
                else:
                    return False

        if len(st) == 0:
            return True       
        else:
            return False
        
s = Solution()
ans = s.isValid("[()]")
print(ans)


# dry run
'''
s = '([)]'
chara = '('
if condition passed --> st = ['(']

chara = '['
if condition passed --> st = ['(', '[']

chara = ')'
if condtion failed --> else part --> top = '[' --> isMatch('[', ')')  --> False
so return False

'''
'''
s = '[()]'
chara = '['
st = ['[']

chara = '('
st = ['[', '(']

chara = ')'
if failed
else --> top = '(' --> isMatch('(', ')') -->returns True --> st.pop --> st = ['[']


chara = ']'
if failed
else --> top = '[' --> isMatch('[', ']') -->returns True --> st.pop --> st = []

'''











