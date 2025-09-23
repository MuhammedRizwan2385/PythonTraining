def binarysearch(list1,k):
    start=0
    end=len(list1)-1
    
    while(start<=end):
        middle=(start+end)//2
        if(list1[middle]==k):
            return middle
        elif(list1[middle]<k):
            
            start=middle+1
        else:
            end=middle-1
            
    
list1=[1,3,5,7]
k=5
print(binarysearch(list1,k))
