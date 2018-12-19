i = 65
s1 = '\0'
s2 = "\0"
s3 = "\0"

while (i <= 90):
    s1 += chr(i)
    i += 1

print(s1)

i = 65
while (i <= 90):
    s1 = chr(i)
    s2 = chr(i + 32)
    s3 += (s1 + s2)
    i += 1

print(s3)
