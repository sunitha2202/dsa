a=[1,2,5,5,5,5,6,7,8]
x=5
first=-1
last=-1
for i in range(len(a)):
    if a[i]==x:
        first=i
        break

for i in range(len(a)):
    if a[i]==x:
        last=i
        
print(first)
print(last)
        