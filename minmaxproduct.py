a=[1,2,34,5,6]
b=[3,7,5,2,4]
max_a=a[0]
min_b=b[0]
for i in range(len(a)):
    if max_a<a[i]:
        max_a=a[i]
for i in range(len(b)):
    if min_b>a[i]:
        min_b=b[i]
print(max_a)
print(min_b)

print(max_a * min_b)