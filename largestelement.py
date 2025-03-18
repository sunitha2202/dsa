a=[1,3,5,7,8]
large=a[0]
for i in range(len(a)):
    if large<a[i]:
        large=a[i]
print(large)