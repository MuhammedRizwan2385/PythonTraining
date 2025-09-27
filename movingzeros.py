l1=[2,0,4,3,0,7,0,6,7,0,3]
for i in l1:
    if i==0:
        l1.remove(i)
        l1.append(i)
print(l1)
