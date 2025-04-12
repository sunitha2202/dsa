class Solution:
    def rotate(self, arr):
        n=len(arr)
        temp=arr[-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        return arr
sol=Solution()
arr=[1,2,3,4,5]
print(sol.rotate(arr))