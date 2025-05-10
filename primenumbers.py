#A simple program to print prime numbers of certain range
def is_prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
            i=i+1
        return True
start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
print(f"The prime numbers between {start}and {end} are:\n")
for i in range(start,end+1):
    if is_prime(i):
        print(i,end=" ")
