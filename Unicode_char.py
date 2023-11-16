# This program take the string S and writes its each character and its unicode point together

S = 'mumbai'
sum = 0
for i in S:
    print(" Character: {0} Unicode Code Point: {1}".format(i, ord(i)))
