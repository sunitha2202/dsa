class Solution:
    def checkSorted(self,a):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                return False
        return True
sol=Solution()
a=[1,2,4,5]
print(sol.checkSorted(a))