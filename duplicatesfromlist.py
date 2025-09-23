list1=[1,2,3,2,4,3]
visit=[]
list_duplicates=[]
for i in list1:
    if i in visit:
        list_duplicates.append(i)
    else:
        visit.append(i)
print(list_duplicates)
