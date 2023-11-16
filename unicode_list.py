# This program take the string S and prints the unicode point of each character as list

S = 'mumbai'

# Using list methods
unicode_S = []
for i in S:
    unicode_S.append(ord(i))
print(unicode_S)

# Using List comprehension
unicode_s = [ord(x) for x in S]
print(unicode_s)

# Using map() function
unicode = map(lambda x: ord(x), S)
print(list(unicode))
