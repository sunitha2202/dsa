a=10
b=5
while a>0 and b>0:
    if a>0:
        a=a%b
    else:
        b=b%a
if a==0:
    print(b)
else:
    print(a)