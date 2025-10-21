#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#for question refer leetcode

 
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        res=0
        while left<=right:
            area=(right-left)*min(height[left],height[right])
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res

        
