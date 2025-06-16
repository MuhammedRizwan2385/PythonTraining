#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*n):
    sum=0
    for i in n:
        sum=sum+i
    average=sum/len(n)
    return(average)
    






if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
