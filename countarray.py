a=[2,3,4,6,5]
evencount=0
oddcount=0
for i in range(len(a)):
    if a[i]%2==0:
        evencount=evencount+1
       
    else:
        
        oddcount=oddcount+1
print(oddcount)
print(evencount)