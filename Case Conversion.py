s = input()
s2 = s[0]
for i in range(1,len(s)):
    if s[i] == s[i].upper():
        s2 += " " + s[i]
    else:
        s2 += s[i]
print(s2)