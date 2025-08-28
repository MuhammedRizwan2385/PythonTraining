#Implement a function to find the second largest number in a list.
def second_largest(nums):
    n=len(nums)
    nums.sort()
    return nums[n-2]
    
nums=[10,20,4,45,99]
print(second_largest(nums))
