a=[1,3,4,5,6,7,8,4]
n=len(a)
k=2
b=[]
if n==1 or k==0 or k==1:
    print(a)
for i in range(n-k,n):
    b.append(a[i])
    
for i in range(n-k):
    b.append(a[i])
    
for i in range(n):
    a[i]=b[i]
print(a)