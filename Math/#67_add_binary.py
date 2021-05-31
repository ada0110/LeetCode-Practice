'''
Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # i and j point to last elem of respective binary strings
        i = len(a) - 1
        j = len(b) - 1

        # As long as the string exists or carry exists
        while(i>=0 or j>=0 or carry):
            total = carry

            if (i >= 0):
                total += int(a[i])      # convert a[i] to int 
                i -= 1

            if (j >= 0):
                total += int(b[j])      # convert b[j] to int
                j -= 1
            
            # when 2 1's are added then result will be zero and carry will be 1 
            # result = 2 % 2 = 0 and carry = 2//2 = 1 
            # and when 3 1's are added then result will be 1 and carry will be 1 
            #  result = 3 % 2 = 1 and carry = 3 // 2 = 1

            result.append(str(total % 2))
            carry = total // 2
        
        # finally reversing the result as we started from LHS
        return ''.join(reversed(result))


        
s = Solution()
ans = s.addBinary("1010","010")
print(ans)  # 1100 