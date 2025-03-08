
def swap_case(s):
    new_string=""
    for i in range(len(s)):
        value=ord(s[i])
        if(97<=value<=122):
            new_string=new_string+s[i].upper()
        elif(65<=value<=90):
            new_string=new_string+s[i].lower()
        else:
            new_string=new_string+s[i]
        
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
