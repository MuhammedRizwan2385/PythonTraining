s1=input();
s2=input();
if(len(s1)!=len(s2)):
    print("Not anagram");
else:
    if sorted(s1.lower())==sorted(s2.lower()):
        print("Anagram")
    else:
        print("Not anagram")
