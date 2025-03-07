# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
sum=0.00
for i in range(n):
    num=float(input())
    sum+=num
    
average=sum/n
print("The average is: {:.2f}".format(average))
