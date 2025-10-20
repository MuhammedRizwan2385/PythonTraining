'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0'''

import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts=collections.Counter(s)
        for i,character in enumerate(s):
            if char_counts[character]==1:
                return i
        return -1
       
       
        
                
        
