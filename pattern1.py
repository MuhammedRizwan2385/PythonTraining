"""A
   A B
   A B C
   ........
   ........"""
n=int(input("Enter the limit: "))
if(n<=26):
    for i in range(1,n+1):
        for j in range(1,i+1):
            j=j+64
            print(chr(j),end=" ")
        print(" ")
