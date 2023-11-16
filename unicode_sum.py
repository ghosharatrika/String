# this program takes the string S and calculate the sum of unicode point of each of its character

S = 'mumbai'
sum = 0
for i in S:
    sum += ord(i)
print("\nSum of unicode code point = ", sum)
