n=36
for i in range(1,n+1):   # print all divisors
   if  n%i==0:
      print(i)
count=0

for i in range(1,n+1):   # count of divisors that divides by 3
    if n%i==0 and i%3==0:
        count=count+1
print(count) 