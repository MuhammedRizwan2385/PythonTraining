# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
copy=n
m=0
while(n>0):
    remainder=n%10
    m=m*10+remainder
    n=int(n/10)

if(copy==m):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
