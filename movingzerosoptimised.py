l1=[2,0,4,3,0,7,0,6,7,0,3]
pos=0
for i in range(len(l1)):
    if l1[i]!=0:
        l1[pos]=l1[i]
        pos+=1
while pos<len(l1):
    l1[pos]=0
    pos+=1
print(l1)
