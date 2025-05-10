#take n numbers from user and find median
n=int(input("enter the limit:"))
a=[]
for i in range(n):
    num=int(input("Enter the number"))
    a.append(num)
a.sort()
m=n//2
if(n%2==0):
    median=(a[m]+a[m-1])/2
else:
    median=a[m]
print("Median is:",median)
