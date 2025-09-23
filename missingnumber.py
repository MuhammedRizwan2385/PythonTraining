"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8"""

arr=[9,6,4,2,3,5,7,0,1]
n=len(arr)
sum_arr=sum(arr)
sum_n=((n*(n+1))//2)
print(sum_n-sum_arr)

