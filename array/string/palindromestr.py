s="madam"
copystr=""
for i in range(len(s)-1,-1,-1):
    copystr+=s[i]
print(copystr)
if s==copystr:
    print(True)
else:
    print(False)
