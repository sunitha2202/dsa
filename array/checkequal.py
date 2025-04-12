class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        
        if len(a) != len(b):
            return False
        n=len(a)

        for i in range(n):
            for j in range(n-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
            
        #print(a)
        for i in range(n):
            for j in range(n-i-1):
                if b[j]>b[j+1]:
                    b[j],b[j+1] = b[j+1],b[j]
            
       # print(b)
        if a == b:
            return True
        else:
            return False
sol=Solution()
a=[5,4,3,1,2]
b=[5,3,4,2,1]
print(sol.checkEqual(a,b))




