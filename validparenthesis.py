
s="([])"
list1=[]
flag=0
for i in s:
    if i=='(' or i=='{' or i=='[':
        list1.append(i)
    elif i==')'or i=='}'or i==']':
        top=list1[-1]
        if not list1:
            flag=1
            break
        if i==')' and top=='(':
            list1.pop()
        elif  i=='}' and top=='{':
            list1.pop()
        elif  i==']' and top=='[':
            list1.pop()
        else:
            flag=1
            break
if flag==0 and not list1:
    print("true")
else:
    print("false")

            
