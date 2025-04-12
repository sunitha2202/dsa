class Solution:
    def checkEqualValue(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        
        a.sort()  # Sort the first array
        b.sort()  # Sort the second array
        
        return a == b
sol=Solution()
a=[4,2,1,3]
b=[1,3,4]
print(sol.checkEqualValue(a,b))