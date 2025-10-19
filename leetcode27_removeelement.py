'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''
'''Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]'''

#by using del (straight forward approach)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        i=0
        while(i<n):
            if nums[i]==val:
                del nums[i]
                n-=1
            else:
                i+=1
        return len(nums)
      
    #by using 2 pointers
  
    class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        for right in range(0,len(nums)):
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
        return left
            
                

        
