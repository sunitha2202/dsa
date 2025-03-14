import math

n=10
    
        # code here
        
if n<2:
    print("not prime")
elif n%2==0:
 
    print("not prime")
else:
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            print("not prime")
            break
        else:

            print("prime")