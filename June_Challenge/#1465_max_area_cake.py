'''
Return the maximum area of a piece of cake after you cut at each horizontal and 
vertical position provided in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a huge number, return this modulo 10^9 + 7.

Ex:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 

horiz: [1,2,4] h=[5]        vert: [1,3] w=[4]
# finding diff between consecutive elems
h_diff: [1,2,1]               w_diff: [2,1]
max(h_diff): 2                max(w_diff): 2
ans: 2*2 = 4 

'''


from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # inserting 0 at the start of array
        horizontalCuts.insert(0,0)
        verticalCuts.insert(0,0)

        # sorting both the arrays
        horizontalCuts_s = sorted(horizontalCuts)
        verticalCuts_s = sorted(verticalCuts)

        # appending h and w in respective arrays
        horizontalCuts_s.append(h)
        verticalCuts_s.append(w)

        print(f"horizonat_sorted: {horizontalCuts_s}    vertical_sorted: {verticalCuts_s}" )
        

    
        # finding out the difference between two consecutive elems for both arrays and storing the max diff
        max_diff_h = 0
        max_diff_v = 0

        for i in range (len(horizontalCuts)):
            diff_h = horizontalCuts_s[i+1]-horizontalCuts_s[i]
            # print(diff_h)
            if diff_h > max_diff_h:
                max_diff_h = diff_h
        print("max_diff_h:", max_diff_h)

        for i in range (len(verticalCuts_s)-1):
            diff_v = verticalCuts_s[i+1]-verticalCuts_s[i]
            # print(diff_v)
            if diff_v > max_diff_v:
                max_diff_v = diff_v
        print("max_diff_v:", max_diff_v)
        

        # # returning their multipliaction
        return (max_diff_h * max_diff_v)% (10**9+7)







s = Solution()
# ans = s.maxArea(h=5, w=4, horizontalCuts=[1,2,4], verticalCuts=[1,3])
# ans = s.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1])
ans = s.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3])
print("max area of cake: ", ans)