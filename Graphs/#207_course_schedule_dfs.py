'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

from typing import List

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # intializing map to store courses and their pre-requisites
        preMap = {i:[] for i in range(numCourses)} 
        print(preMap)

        # initializing visited set to add all courses along the dfs path
        visited = set()

        # adding the courses and pre-requisites into preMap
        for crs, pre in prerequisites:
           preMap[crs].append(pre)
        # print(preMap)
        
        # function to check pre satisfied or not
        def dfs(crs):
            # if crs is already in visited set and we are visiting again means  
            # there is a loop so return false
            if crs in visited:
                return False

            # if the pre-requisit is none then return true
            if preMap[crs] == []:
                return True
            
            # add crs to visited set and check for its preq recursively
            visited.add(crs)
            for pre in preMap[crs]:
                # if crs can't be taken 
                if not dfs(pre): return False

            # if the crs can be taken then return true
            # remove crs from visited set as we are not visiting it any more and done visiting
            # set its preq as none as we have already satified preq
            visited.remove(crs)
            preMap[crs] = []
            return True


        # selecting crs one by one and checking whether the pre is satisfied
        # this works for disconnected graph as well 
        # 1 -> 2
        # 3 -> 4 so check for each crs independently 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True



s = Solution()
ans = s.canFinish( 2, [[1,0],[0,1]]) #(5, [[0,1], [0,2], [1,3], [1,4], [3,4]])
print(ans)