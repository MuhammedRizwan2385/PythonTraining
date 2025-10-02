#reversing the vowels of a string
#Input: s = "practice"
#Output: "prectica"
#Explanation: The vowels are a, i, e. Reverse of these is e, i, a.
#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        start=0
        end=len(s)-1
        s1=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while start<end:
            while start<end and s[start] not in vowels:
                start+=1
            while start<end and s[end] not in vowels:
                end-=1
            s1[start],s1[end]=s1[end],s1[start]
            start+=1
            end-=1
        return "".join(s1)
