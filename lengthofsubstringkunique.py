s="aabbcc"
k=2
left=0
length=0
for right in range(len(s)):
    substring=s[left:right+1]
    uniquecharacter=set(substring)
    while len(uniquecharacter)>k:
        left=left+1
        substring=s[left:right+1]
        uniquecharacter=set(substring)
    if len(uniquecharacter)==k:
        length=max(length,right-left+1)
print(length)
        
    
