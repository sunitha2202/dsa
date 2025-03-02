n=54545
sum=0
x=n
while n>0:
    ld=n%10
    sum=sum*10+ld
    n=n//10
if sum==x:
    print("is palindrome")
else:
    print("not a palindrome")