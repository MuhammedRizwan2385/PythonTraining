def merge_sorted_list(a,b):
    i=j=k=0
    n,m=len(a),len(b)
    result=[0]*(n+m)
    while i<n and j<m:
        if a[i]<b[j]:
            result[k]=a[i]
            i+=1
            k+=1
        else:
            result[k]=b[j]
            j+=1
            k+=1
    while(i<n):
          result[k]=a[i]
          i+=1
          k+=1
    while(j<m):
          result[k]=b[j]
          j+=1
          k+=1
    return result
list1=[1,3,5]
list2=[2,4,6]
print(merge_sorted_list(list1,list2))
