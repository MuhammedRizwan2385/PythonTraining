''' Count unique characters in a string.
Answer: Use a set or collections.Counter to count unique chars.
Test: "hello" → 4'''

s="hello"
uniquecharacters=set(s)
print(len(uniquecharacters))
print(uniquecharacters)
