# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a=float(input())
b=float(input())
c=float(input())

if(a+c>b or b+c>a or a+b>c):
    s=(a+b+c)/2
    area=((s*(s-a)*(s-b)*(s-c)))
    if(area>0):
        print("The area of the triangle is: {:.2f}".format(math.sqrt(area)))
    else:
        print("Invalid Triangle")

    
