# Enter your code here. Read input from STDIN. Print output to STDOUT
vowels=['A','a','E','e','I','i','O','o','U','u']
string=input()
count=0
for i in range(len(string)):
    if(string[i] in vowels):
        count=count+1
if(count>0):
    print("Total number of vowels:",count)
else:
    print("No vowels were found.")
